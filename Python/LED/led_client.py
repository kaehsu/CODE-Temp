#!/usr/bin/env python3
#
# To communicate with UDS server by nc: "echo -e "string\c" | sudo nc -q 1 -U /var/run/uds_led"

import socket
from pprint import pprint
serverAddress = '/tmp/portex_led'


def main():
    try:
        while True:
            message = input(
                '\nEnter the message send to the server \n("Quit" to quit): ')
            try:
                if message:
                    if message == 'Quit':
                        raise SystemExit
                    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    sock.connect(serverAddress)
                    sock.send(message.encode('utf-8'))
                    recvMessage = sock.recv(1024).decode('utf-8')
                    try:
                        pprint(eval(recvMessage))
                        sock.close()
                    except (SyntaxError, NameError):
                        print(recvMessage)
                        sock.close()
                else:
                    print('You have to enter something.....\n')
                    continue
            except ConnectionRefusedError:
                print('\n The LED socket connection refused')
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    main()
