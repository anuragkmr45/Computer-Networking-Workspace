# Numerical solutions

The arithmetic follows the explicitly defined exercise models. Delay/BDP equations are dimensional reasoning; protocol-specific boundaries are grounded in the starter sources (RFC9293 and RFC1812). The included tests independently check representative quantities, address allocations, offsets, and the CRC.

## N01
L = 1500 x 8 = 12,000 bits. t = 12,000 / 100,000,000 = 0.00012 s = 0.12 ms = 120 microseconds.

## N02
Distance = 1,000,000 m. t = 1,000,000 / 200,000,000 = 0.005 s = 5 ms.

## N03
Serialization per link = 1.2 ms. Total = 3 x 1.2 + 3 x 2 = 9.6 ms. Each router must receive the complete packet in this model.

## N04
The first packet arrives at 9.6 ms; equal-rate pipelining delivers subsequent packets at 1.2-ms intervals. Last = 9.6 + 3 x 1.2 = 13.2 ms; equivalently (3+4-1)x1.2+6.

## N05
Mask 255.255.255.192. Network 192.168.10.128/26; broadcast .191; usable .129–.190, 62 hosts. Last-octet AND: 10000010 & 11000000 = 10000000.

## N06
/16: both AND results 192.168.0.0, so on-link under the model. /24: 192.168.10.0 versus 192.168.11.0, so default gateway selected. The destination IP does not become the gateway IP.

## N07
100 hosts -> /25: 10.20.30.0/25, usable .1–.126. 50 -> /26: .128/26, usable .129–.190. 20 -> /27: .192/27, usable .193–.222. Remaining .224/27 is unused. Counts: 126, 62, 30.

## N08
10.20.30.150 -> C (/25). 10.20.30.20 -> B (/16). 203.0.113.5 -> D (/0). Choose the longest eligible matching prefix, not the shortest printed address.

## N09
100,000,000 x 0.040 = 4,000,000 bits = 500,000 bytes. This is a modeled in-flight volume, not a direct buffer-tuning recommendation.

## N10
64,000 x 8 / 0.080 = 6,400,000 bits/s = 6.4 Mbps. min(100,6.4) = 6.4 Mbps; real throughput may be lower.

## N11
Tdata = 8 ms. Cycle = 8+20 = 28 ms. U = 8/28 = 2/7, about 28.57%. Data rate = 8,000/0.028 = about 285,714 bits/s.

## N12
Window >= ceil((8+20)/8) = ceil(3.5) = 4 frames under the stated ACK timing and no-loss model. This is not a universal TCP window rule.

## N13
Efficiency = 1000/(1000+50) = 20/21 = about 95.238%. Real Ethernet/TCP/TLS overhead requires a different explicitly specified model.

## N14
Original payload = 3,980 bytes. Non-final payload cap = floor((1500-20)/8)x8 = 1,480. Payloads: 1480,1480,1020; total lengths: 1500,1500,1040. Offsets: 0,185,370. MF: 1,1,0. Verify payload sum 3980.

## N15
After first range, ACK 2001. After second, ACK 2501. These acknowledge the next expected byte, not the last received byte. Assumptions exclude SYN/FIN sequence-space consumption.

## N16
Generator degree is 3; divide 1101000 by 1011 using XOR. 1101000 XOR 1011000 = 0110000; XOR 0101100 = 0011100; XOR 0010110 = 0001010; XOR 0001011 = 0000001. Remainder 001. Codeword 1101001 divides with zero remainder.
