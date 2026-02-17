import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
    )

server.bind((HOST, PORT))
server.listen(1)

print("Waiting...")
conn, addr = server.accept()
print("Connected:", addr)

conn.sendall(b"Hello from WSL2!")
conn.close()
