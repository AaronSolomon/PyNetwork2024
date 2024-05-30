
#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# http://ipv6.ncnu.org/Course/PythonNetworkProgramming/Code/ch03_tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, time, random, zmq

def server(host = '127.0.0.1', port = 1060, interval=1):
    # interval is only useful in client
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(url)
    while True:
        req = socket.recv_string()
        msg = "Ack {}".format(req.rsplit(maxsplit=1)[-1])
        socket.send_string( msg )
    

def client(host, port, interval):
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(url)
    n = random.randint(1, 9)
    for i in range(n):
        msg = "Agent.{1} is sending {0}/{1}".format(i, n)
        socket.send_string( msg )
        time.sleep(interval)    
        print( socket.recv_string() )

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='ZeroMQ Req/Resp')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    parser.add_argument('-i', metavar='INTERVAL', type=int, default=1,
                        help='Time interval (default 1)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.i)
