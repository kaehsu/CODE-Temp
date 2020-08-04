#!/usr/bin/env python3
#
# To communicate with UDS server by nc: "echo -e "string\c" | sudo nc -q 1 -U /var/run/uds_led"

import socket
serverAddress = '/tmp/portex_led'


def main():
    try:
        while True:
            message = input(
                'Enter the message send to server ("Quit" to quit): ')
            if message:
                if message == 'Quit':
                    raise SystemExit
                sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                sock.connect(serverAddress)
                sock.send(message.encode('utf-8'))
                #r = sock.recv(1024)
                print('Receiving message "{}" from server.\n'.format(
                    sock.recv(1024).decode()))
                sock.close()
            else:
                print('You have to enter something.....\n')
                continue
    except KeyboardInterrupt:
        print('\n')
        # sock.close()


if __name__ == '__main__':
    main()
