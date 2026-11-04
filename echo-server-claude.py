import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 28333

body = "Hello!"
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    f"Content-Length: {len(body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
    f"{body}"
)

with socket.socket() as s:
    # Lets us restart the server right away without "Address already in use"
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")

    while True:
        new_con = s.accept()
        new_sock = new_con[0]  # new_con[1] is the client's address

        with new_sock:
            print(f"Connected by {new_con[1]}")

            request = b""
            # The request header ends with a blank line
            while b"\r\n\r\n" not in request:
                chunk = new_sock.recv(4096)
                if not chunk:  # client closed the connection early
                    break
                request += chunk

            print(request.decode("ISO-8859-1"))
            new_sock.sendall(response.encode("ISO-8859-1"))
