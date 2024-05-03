#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_single.py
# Single-threaded server that serves one client at a time; others must wait.

import ch07_zen_utils

if __name__ == '__main__':
    address = ch07_zen_utils.parse_command_line('simple single-threaded server')
    listener = ch07_zen_utils.create_srv_socket(address)
    ch07_zen_utils.accept_connections_forever(listener)
