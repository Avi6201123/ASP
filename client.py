import socket
import sys

HOST = "127.0.0.1"
PORT = 9999
if len(sys.argv) >= 2:
    HOST = sys.argv[1]
if len(sys.argv) >= 3:
    PORT = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}. Type messages; 'exit' to quit.")
    try:
        while True:
            msg = input("> ").strip()
            if not msg:
                continue
            s.sendall((msg + "\n").encode())
            data = s.recv(4096)
            if not data:
                print("Server closed connection.")
                break
            resp = data.decode(errors="replace").strip()
            print("Server:", resp)
            if msg.lower() == "exit":
                print("Exiting client.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupted — closing.")
