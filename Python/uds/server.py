import socket

server_addr = '/tmp/server.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_addr)
sock.listen(0)

while True:
    conn, clientAddr = sock.accept()
    while True:
        data = conn.recv(100)
        conn.sendall(data)
