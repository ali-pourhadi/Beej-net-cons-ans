import socket
import sys

if len(sys.argv) < 2:
    sys.exit(f"Usage: python {sys.argv[0]} <host> [port]")

host = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

# Header ends with a blank line (\r\n\r\n), which tells the server we're done
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

data = b""
with socket.socket() as s:
    s.connect((host, port))
    s.sendall(request.encode("ISO-8859-1"))

    # ":=" is the walrus operator: it assigns the result of recv() to chunk
    # and also returns it, so the while can test it in the same step.
    # recv() returns b"" (falsy) once the server closes the connection,
    # which ends the loop.
    while chunk := s.recv(4096):
        data += chunk

print(data.decode("ISO-8859-1"))
