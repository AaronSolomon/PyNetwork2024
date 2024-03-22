#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# http://ipv6.ncnu.org/Course/PythonNetworkProgramming/Code/ch03_tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket

MAXBUF = 65535

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def server(interface, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listeningSock.bind((interface, port))
    listeningSock.listen(1)
    print('Listening at', listeningSock.getsockname())
    sock, sockname = listeningSock.accept()
    while True:
        data = sock.recv(MAXBUF)
        if data == b'': break
        print(data.decode())
    sock.close()

def client(host, port):
    name = input("Your name? ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        msg = input("> ")
        if msg == '': break
        data = bytes("[{}] {}".format(name, msg), 'UTF-8')
        sock.send(data)
    sock.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
