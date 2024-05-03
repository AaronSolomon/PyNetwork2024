#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_threaded.py
# Using multiple threads to serve several clients in parallel.

import ch07_zen_utils
from threading import Thread

def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=ch07_zen_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = ch07_zen_utils.parse_command_line('multi-threaded server')
    listener = ch07_zen_utils.create_srv_socket(address)
    start_threads(listener)
