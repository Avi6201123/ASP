import socket

HOST = "0.0.0.0"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT} — waiting for one client...")
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(4096)
            if not data:
                print("Client disconnected.")
                break
            text = data.decode(errors="replace").strip()
            print("Client:", text)
            if text.lower() == "exit":
                print("Exit received — closing.")
                conn.sendall(b"bye\n")
                break
            # echo back with prefix
            reply = f"Server received: {text}\n"
            conn.sendall(reply.encode())
