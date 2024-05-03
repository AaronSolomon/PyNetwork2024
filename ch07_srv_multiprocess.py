#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_multiprocess.py
# Using multiple processes to serve several clients in parallel.

import ch07_zen_utils
from multiprocessing import Process

def start_processes(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Process(target=ch07_zen_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = ch07_zen_utils.parse_command_line('multi-processed server')
    listener = ch07_zen_utils.create_srv_socket(address)
    start_processes(listener)
