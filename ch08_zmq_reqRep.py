
#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# http://ipv6.ncnu.org/Course/PythonNetworkProgramming/Code/ch03_tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, zmq

def server(host = '127.0.0.1', port = 1060):
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(url)
    req = socket.recv_string()
    print("Received: {}".format(req))
    response = "I am OK!"
    socket.send_string(response)
    

def client(host, port):
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(url)
    socket.send_string('Are you OK?')
    response = socket.recv_string();
    print("response: " + response)

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='ZeroMQ Req/Resp')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
