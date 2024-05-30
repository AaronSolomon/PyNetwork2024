
#!/usr/bin/env python3
# Broadcast to all subscribers.  The publisher does not buffer the message.

import argparse, zmq, time, random

def publisher(host = '127.0.0.1', port = 1060):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(url)
    for i in range(10):
        time.sleep(0.5)
        msg = "Broadcast {}".format(i+1)
        print(msg)
        req = socket.send_string(msg)
    socket.send_string("EOF")

def subscriber(host, port):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(url)
    socket.setsockopt_string(zmq.SUBSCRIBE,'')
    # Without this filter, all messages will be excluded.
    # If the filter string is '', all messages are received.
    # If the filter string is 'a', all messages with prefix 'a' are received.
    # If you run setsockopt() again to add another prefix 'b',
    # messages begins with 'a' or 'b' will be received.

    while True:
        time.sleep( random.randint(1,5) )
        msg = socket.recv_string();
        print("Message: " + msg)
        if msg == "EOF":
            break

if __name__ == '__main__':
    choices = {'subscriber': subscriber, 'publisher': publisher}
    parser = argparse.ArgumentParser(description='ZeroMQ Pub/Sub')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='hostname of the publisher')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
