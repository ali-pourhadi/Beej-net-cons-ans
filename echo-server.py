import sys, socket

HOST = "127.0.0.1"
PORT = 28333 if len(sys.argv) != 2 else int(sys.argv[1])

body = "Hello!"
message = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(body)}\r\nConnection: close\r\n\r\n{body}"

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    while True :
        new_con = s.accept()
        new_sock = new_con[0]
        with new_sock:
            print(f"connected by {new_con[1]}")
            res = ""
            while True :
                data = new_sock.recv(4096)
                if len(data) == 0 :
                    break
                res += data.decode("ISO-8859-1")
                if "\r\n\r\n" in res :
                    break
            print (res)
            new_sock.sendall(message.encode("ISO-8859-1"))
