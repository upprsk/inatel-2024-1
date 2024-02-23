import socket
import sys
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET


def main() -> None:
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <addr> <port>")
        sys.exit(1)

    addr = sys.argv[1]
    port = int(sys.argv[2])

    with socket.socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        sock.connect((addr, port))
        print(f"Connected to server at {addr}:{port}")

        while True:
            packet = sock.recv(1024)
            if packet == b"":
                print("Server disconnected!")
                sys.exit(1)

            prompt = packet.decode(errors="ignore")
            print(prompt)

            if packet[-1] == 0xFF:
                break

            res = input("> ")
            sock.send(res.encode())


if __name__ == "__main__":
    main()
