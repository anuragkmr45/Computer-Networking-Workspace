"""Deterministic arithmetic checks for the original practice models."""
import ipaddress
import math
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
from netcalc import subnet_info, delay, bdp, crc_encode, poly_mod, ipv4_fragments

class Calculations(unittest.TestCase):
    def test_n01_serialization(self): self.assertAlmostEqual(delay(1500,100)['serialization_s'],0.00012)
    def test_n02_propagation(self): self.assertAlmostEqual(delay(1,100,1000)['propagation_s'],0.005)
    def test_n03_store_forward(self): self.assertAlmostEqual(3*delay(1500,10)['serialization_s']+3*.002,.0096)
    def test_n04_pipeline(self): self.assertAlmostEqual((3+4-1)*delay(1500,10)['serialization_s']+.006,.0132)
    def test_n05_subnet(self):
        x=subnet_info('192.168.10.130/26')
        self.assertEqual((x['network'],x['broadcast'],x['model_host_count']),('192.168.10.128','192.168.10.191',62))
    def test_n06_slash16(self): self.assertTrue(subnet_info('192.168.10.20/16','192.168.11.80')['destination_in_connected_prefix'])
    def test_n06_slash24(self): self.assertFalse(subnet_info('192.168.10.20/24','192.168.11.80')['destination_in_connected_prefix'])
    def test_n07_vlsm(self):
        nets=[ipaddress.ip_network(n) for n in ['10.20.30.0/25','10.20.30.128/26','10.20.30.192/27']]
        self.assertEqual([n.num_addresses-2 for n in nets],[126,62,30])
        self.assertTrue(all(n.subnet_of(ipaddress.ip_network('10.20.30.0/24')) for n in nets))
        self.assertFalse(any(a.overlaps(b) for i,a in enumerate(nets) for b in nets[i+1:]))
    def test_n08_routes(self):
        routes=[(ipaddress.ip_network(n),v) for n,v in [('10.0.0.0/8','A'),('10.20.0.0/16','B'),('10.20.30.128/25','C'),('0.0.0.0/0','D')]]
        results=[max((r for r in routes if ipaddress.ip_address(d) in r[0]), key=lambda r:r[0].prefixlen)[1] for d in ['10.20.30.150','10.20.30.20','203.0.113.5']]
        self.assertEqual(results,['C','B','D'])
    def test_n09_bdp(self): self.assertEqual(bdp(100,40),{'bits':4000000.0,'bytes':500000.0})
    def test_n10_window(self): self.assertEqual(min(100e6,64000*8/.08),6.4e6)
    def test_n11_stopwait(self): self.assertAlmostEqual(.008/(.008+.020),2/7)
    def test_n12_window_frames(self): self.assertEqual(math.ceil((.008+.020)/.008),4)
    def test_n13_overhead(self): self.assertAlmostEqual(1000/1050,20/21)
    def test_n14_fragments(self):
        self.assertEqual(ipv4_fragments(4000,1500),[
            {'payload':1480,'total':1500,'offset':0,'mf':1},
            {'payload':1480,'total':1500,'offset':185,'mf':1},
            {'payload':1020,'total':1040,'offset':370,'mf':0}])
    def test_n15_ack(self): self.assertEqual((1001+1000,1001+1000+500),(2001,2501))
    def test_n16_crc(self):
        result=crc_encode('1101','1011')
        self.assertEqual((result['remainder'],result['codeword'],result['verification_remainder']),('001','1101001','000'))
    def test_slash31(self):
        x=subnet_info('192.0.2.0/31'); self.assertEqual(x['model_host_count'],2); self.assertIsNone(x['broadcast'])
    def test_slash32(self):
        x=subnet_info('192.0.2.7/32'); self.assertEqual(x['model_host_count'],1); self.assertEqual(x['network'],'192.0.2.7')
    def test_invalid_address(self):
        with self.assertRaises(ValueError): subnet_info('999.1.1.1/24')
    def test_reject_ipv6_for_ipv4_exercise(self):
        with self.assertRaises(ValueError): subnet_info('2001:db8::1/64')
    def test_bad_rate(self):
        with self.assertRaises(ValueError): delay(1500,0)
    def test_bad_distance(self):
        with self.assertRaises(ValueError): delay(1500,100,-1)
    def test_nonfinite(self):
        with self.assertRaises(ValueError): bdp(float('nan'),40)
    def test_bad_generator(self):
        with self.assertRaises(ValueError): crc_encode('1101','0010')
    def test_bad_bits(self):
        with self.assertRaises(ValueError): poly_mod('1201','1011')
    def test_unfragmented(self): self.assertEqual(ipv4_fragments(1000,1500),[{'payload':980,'total':1000,'offset':0,'mf':0}])
    def test_bad_mtu(self):
        with self.assertRaises(ValueError): ipv4_fragments(4000,20)

if __name__=='__main__': unittest.main()
