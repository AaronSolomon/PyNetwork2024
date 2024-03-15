import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ('localhost', 11000) )
sock.connect(('localhost', 1060) )
sock.close()
