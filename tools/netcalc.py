#!/usr/bin/env python3
"""Offline learning calculators. Python 3.10+, standard library, no network calls."""
from __future__ import annotations
import argparse
import ipaddress
import json
import math
from typing import Any


def positive(value: float, name: str) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be finite and greater than zero')
    return value


def subnet_info(cidr: str, destination: str | None = None) -> dict[str, Any]:
    interface = ipaddress.IPv4Interface(cidr)
    net = interface.network
    if net.prefixlen < 31:
        first, last = int(net.network_address) + 1, int(net.broadcast_address) - 1
        hosts = net.num_addresses - 2
        interpretation = 'Conventional IPv4 LAN; provider-specific reservations excluded.'
    else:
        first, last, hosts = int(net.network_address), int(net.broadcast_address), net.num_addresses
        interpretation = '/31 point-to-point interpretation or /32 single address; verify applicability.'
    result: dict[str, Any] = {
        'address': str(interface.ip), 'prefix': net.prefixlen, 'mask': str(net.netmask),
        'network': str(net.network_address), 'cidr': str(net),
        'broadcast': str(net.broadcast_address) if net.prefixlen < 31 else None,
        'addresses': net.num_addresses, 'model_host_count': hosts,
        'first_model_host': str(ipaddress.IPv4Address(first)),
        'last_model_host': str(ipaddress.IPv4Address(last)), 'interpretation': interpretation,
    }
    if destination is not None:
        dst = ipaddress.IPv4Address(destination)
        result['destination'] = str(dst)
        result['destination_masked_network'] = str(ipaddress.IPv4Address(int(dst) & int(net.netmask)))
        result['destination_in_connected_prefix'] = dst in net
        result['limitation'] = 'Prefix test only; not actual route selection, VLAN reachability, or return-path proof.'
    return result


def delay(packet_bytes: float, mbps: float, km: float = 0.0, speed_mps: float = 2e8) -> dict[str, float]:
    positive(packet_bytes, 'packet bytes'); positive(mbps, 'Mbps'); positive(speed_mps, 'signal speed')
    if not math.isfinite(km) or km < 0:
        raise ValueError('distance must be finite and nonnegative')
    serialization = packet_bytes * 8 / (mbps * 1e6)
    propagation = km * 1000 / speed_mps
    return {'serialization_s': serialization, 'propagation_s': propagation,
            'one_link_model_total_s': serialization + propagation}


def bdp(mbps: float, rtt_ms: float) -> dict[str, float]:
    positive(mbps, 'Mbps'); positive(rtt_ms, 'RTT milliseconds')
    bits = mbps * 1e6 * rtt_ms / 1000
    return {'bits': bits, 'bytes': bits / 8}


def poly_mod(bits: str, generator: str) -> str:
    if not bits or set(bits) - {'0', '1'}:
        raise ValueError('data must be a nonempty binary string')
    if len(generator) < 2 or set(generator) - {'0', '1'} or generator[0] != '1' or generator[-1] != '1':
        raise ValueError('generator must be binary, degree >= 1, with leading and trailing 1')
    degree = len(generator) - 1
    work = list(map(int, bits.zfill(len(generator))))
    divisor = list(map(int, generator))
    for index in range(len(work) - degree):
        if work[index]:
            for offset, bit in enumerate(divisor):
                work[index + offset] ^= bit
    return ''.join(map(str, work[-degree:]))


def crc_encode(data: str, generator: str) -> dict[str, str]:
    # Validate before constructing the augmented dividend.
    poly_mod(data, generator)
    remainder = poly_mod(data + '0' * (len(generator) - 1), generator)
    codeword = data + remainder
    return {'data': data, 'generator': generator, 'remainder': remainder,
            'codeword': codeword, 'verification_remainder': poly_mod(codeword, generator)}


def ipv4_fragments(total_length: int, mtu: int, header: int = 20) -> list[dict[str, int]]:
    """Educational fixed-header model; no options-copy rules or DF processing."""
    if not 20 <= header <= 60 or header % 4:
        raise ValueError('header must be 20..60 bytes and divisible by 4')
    if not header <= total_length <= 65535 or mtu <= header:
        raise ValueError('invalid IPv4 total length or MTU')
    payload = total_length - header
    if total_length <= mtu:
        return [{'payload': payload, 'total': total_length, 'offset': 0, 'mf': 0}]
    capacity = (mtu - header) // 8 * 8
    if capacity < 8:
        raise ValueError('MTU cannot hold a non-final fragment payload')
    result, sent = [], 0
    while sent < payload:
        amount = min(capacity, payload - sent)
        result.append({'payload': amount, 'total': amount + header,
                       'offset': sent // 8, 'mf': int(sent + amount < payload)})
        sent += amount
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('subnet', help='IPv4 mask calculation, not real routing')
    p.add_argument('cidr'); p.add_argument('--destination')
    p = sub.add_parser('delay', help='One-link serialization + propagation model')
    p.add_argument('--bytes', type=float, required=True); p.add_argument('--mbps', type=float, required=True)
    p.add_argument('--km', type=float, default=0); p.add_argument('--speed', type=float, default=2e8)
    p = sub.add_parser('bdp', help='Bandwidth-delay product')
    p.add_argument('--mbps', type=float, required=True); p.add_argument('--rtt-ms', type=float, required=True)
    p = sub.add_parser('crc', help='Educational binary-polynomial CRC')
    p.add_argument('data'); p.add_argument('generator')
    p = sub.add_parser('fragment', help='Fixed-header educational IPv4 fragmentation')
    p.add_argument('--total', type=int, required=True); p.add_argument('--mtu', type=int, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'subnet': result = subnet_info(args.cidr, args.destination)
        elif args.command == 'delay': result = delay(args.bytes, args.mbps, args.km, args.speed)
        elif args.command == 'bdp': result = bdp(args.mbps, args.rtt_ms)
        elif args.command == 'crc': result = crc_encode(args.data, args.generator)
        else: result = ipv4_fragments(args.total, args.mtu)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
