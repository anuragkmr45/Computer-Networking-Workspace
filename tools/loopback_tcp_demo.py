#!/usr/bin/env python3
"""One bounded TCP echo exchange on 127.0.0.1. No external network connection."""
from __future__ import annotations
import argparse
import json
import queue
import socket
import threading
from typing import Any

LIMIT = 65536
TIMEOUT = 5.0


def receive_all(sock: socket.socket, chunk_size: int) -> tuple[bytes, int]:
    pieces: list[bytes] = []
    count = size = 0
    while True:
        part = sock.recv(chunk_size)
        if not part:
            break
        count += 1; size += len(part)
        if size > LIMIT:
            raise ValueError('bounded demonstration input exceeded')
        pieces.append(part)
    return b''.join(pieces), count


def run_demo(message: str = 'hello networking', chunk_size: int = 4) -> dict[str, Any]:
    payload = message.encode('utf-8')
    if not payload or len(payload) > 4096:
        raise ValueError('message must encode to 1..4096 bytes')
    if not 1 <= chunk_size <= 4096:
        raise ValueError('chunk_size must be 1..4096')
    outcome: queue.Queue[dict[str, Any] | BaseException] = queue.Queue()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.settimeout(TIMEOUT)
        listener.bind(('127.0.0.1', 0))
        listener.listen(1)
        server_address = listener.getsockname()
        def serve() -> None:
            try:
                conn, peer = listener.accept()
                with conn:
                    conn.settimeout(TIMEOUT)
                    data, reads = receive_all(conn, chunk_size)
                    conn.sendall(data)
                    conn.shutdown(socket.SHUT_WR)
                    outcome.put({'client_endpoint': list(peer), 'server_receive_calls': reads,
                                 'server_bytes': len(data)})
            except BaseException as exc:
                outcome.put(exc)
        thread = threading.Thread(target=serve, daemon=True)
        thread.start()
        try:
            with socket.create_connection(server_address, timeout=TIMEOUT) as client:
                client.sendall(payload)
                client.shutdown(socket.SHUT_WR)
                received, reads = receive_all(client, chunk_size)
        finally:
            thread.join(TIMEOUT + 1)
        if thread.is_alive():
            raise RuntimeError('server thread did not finish within the bounded demonstration')
        server_result = outcome.get_nowait()
        if isinstance(server_result, BaseException):
            raise RuntimeError(f'loopback server failed: {server_result}') from server_result
        return {'server_endpoint': list(server_address), **server_result,
                'client_bytes_sent': len(payload), 'client_bytes_received': len(received),
                'client_receive_calls': reads, 'echo_matches': received == payload,
                'note': 'Receive-call counts are application observations, not Ethernet/TCP packet counts.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--message', default='hello networking')
    parser.add_argument('--chunk-size', type=int, default=4)
    args = parser.parse_args()
    try:
        print(json.dumps(run_demo(args.message, args.chunk_size), indent=2))
    except (OSError, ValueError, RuntimeError, queue.Empty) as exc:
        parser.exit(1, f'Demo could not complete: {exc}\nDo not disable security controls; use the paper explanation instead.\n')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
