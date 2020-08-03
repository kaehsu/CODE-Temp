#!/usr/bin/env python3

import socket
import time
ADDR = '/tmp/uds_tmp'


def main():
    try:
        while True:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ADDR)
            message = 'Please give me temprature data'
            sock.send(message.encode('utf-8'))
            #r = sock.recv(1024)
            print('{}'.format(sock.recv(1024)))
            time.sleep(1)
    finally:
        sock.close()


if __name__ == '__main__':
    main()
