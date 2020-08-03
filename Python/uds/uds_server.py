#!/usr/bin/env python3

import os
import socket
import random
ADDR = '/tmp/uds_tmp'


def main():
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists(ADDR):
            os.unlink(ADDR)
        sock.bind(ADDR)
        sock.listen(5)
        while True:
            connection, address = sock.accept()
            #print('Data : {}'.format(connection.recv(1024)))
            randomN = random.randint(1, 100)
            message = str(randomN)
            connection.send(message.encode('utf-8'))
            connection.close()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
