import socket
import time

server_addr = '/tmp/server.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(server_addr)

while True:
    message = 'hello world!'
    sock.sendall(message.encode('utf-8'))
    sock.recv(100)
    time.sleep(1)

sock.close()
