
#!/usr/bin/env python3
# When the server pushes data, it awaits a client to pull it.
# Multiple clients will compete with each other.  Only one gets the data.

# If the client bind() and the server connect(), then after the server
# pushes, even if the client has not pulled, the data is stored in the
# client's buffer, so the server can push next item without blocking.
# However, it is unreasonable for client to bind(), because in that
# case, only one client will handle the task pushed by the server.

import argparse, zmq, time

def push(host = '127.0.0.1', port = 1060):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind(url)
    for i in range(10):
        time.sleep(0.5)
        msg = "Broadcast {}".format(i+1)
        print(msg)
        req = socket.send_string(msg)
    socket.send_string("EOF")
    socket.send_string("EOF")

def pull(host, port):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect(url)
    #socket.setsockopt_string(zmq.SUBSCRIBE,'')
    # Without this filter, all messages will be excluded.
    # If the filter string is '', all messages are received.
    # If the filter string is 'a', all messages with prefix 'a' are received.
    # If you run setsockopt() again to add another prefix 'b',
    # messages begins with 'a' or 'b' will be received.

    while True:
        time.sleep(1)
        msg = socket.recv_string();
        print("Message: " + msg)
        if msg == "EOF":
            break

if __name__ == '__main__':
    choices = {'pull': pull, 'push': push}
    parser = argparse.ArgumentParser(description='ZeroMQ Pub/Sub')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='hostname of the message queue')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
