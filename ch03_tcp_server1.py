import socket
listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listeningSock.bind(('localhost', 1060))
listeningSock.listen(1)
sock, sockname = listeningSock.accept()
print("Connecting from", sock.getpeername())
sock.close()
listeningSock.close()
