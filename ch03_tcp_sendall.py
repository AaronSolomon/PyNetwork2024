
#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# http://ipv6.ncnu.org/Course/PyNetwork/Code/ch03_tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket
MAXBYTES = 65536

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

def server(interface, port, nSize):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listeningSock.bind((interface, port))
    listeningSock.listen(1)
    print('Listening at', listeningSock.getsockname())
    while True:
        print('Waiting to accept a new connection')
        sock, sockname = listeningSock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sock.getsockname())
        print('  Socket peer:', sock.getpeername())
        while True:
            n = len(sock.recv(MAXBYTES))
            if n == 0: break
            print("Receiving {} bytes".format(n))

def client(host, port, nSize):
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    nSize = 0
    while True:
        nSize += 1
        data = bytes(nSize)
        n = sock.send(data)
        fmt = "{}/{} sent"
        print(fmt.format(n, len(data)))
        if n != len(data): break
    time.sleep(3)

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    parser.add_argument('-n', metavar='SIZE', type=int, default=1000,
                        help='Data size (default 1000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.n)
