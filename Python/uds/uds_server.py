#!/usr/bin/env python3

import os
import sys
import socket
serverAddress = '/tmp/portex_tmp'

dictForquery = {
    "gLED": "Green LED",
    "rLED": "Red LED",
    "bLED": "Blue LED",
    "yLED": "Yellow LED",
    "oLED": "Orange LED"
}


def main():
    try:
        # Check the socket status
        if os.path.exists(serverAddress):
            os.unlink(serverAddress)
        # Create the Unix Domain Socket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Bind the UDS to the port
        print('Starting up an UDS for portex testing on {}.....'.format(
            serverAddress), file=sys.stderr)
        sock.bind(serverAddress)
        # Listen the port
        sock.listen(5)
        # Process the incoming packet
        while True:
            connection, address = sock.accept()
            serverIncoming = connection.recv(1024)
            print('Receving data "{}" from client.....'.format(
                serverIncoming.decode()))
            # connection.send(message.encode('utf-8'))      # Regular data should be encode before send
            # Received data is encoded, can send directly
            # connection.send(serverIncoming)
            if serverIncoming.decode() in dictForquery.keys():
                serverOutput = dictForquery[serverIncoming.decode()]
                connection.send(serverOutput.encode('utf-8'))
            else:
                serverOutput = 'Not a valid command.'
                connection.send(serverOutput.encode('utf-8'))
            connection.close()
    except KeyboardInterrupt:
        print('The server daemon stop!', file=sys.stderr)
        sock.close()


if __name__ == '__main__':
    main()
