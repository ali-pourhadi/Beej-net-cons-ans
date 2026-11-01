import sys, socket

if len(sys.argv) >= 3 :
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
elif len(sys.argv) == 2 : 
    HOST = sys.argv[1]
    PORT = 80
else : 
    HOST = '127.0.0.1'
    PORT = 12345
    
message = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
ans = ""
with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode("ISO-8859-1"))
    while True:
        res = s.recv(4096)
        ans += res.decode("ISO-8859-1")
        if len(res) == 0 :
            break
print (ans)

