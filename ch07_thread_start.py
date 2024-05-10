import threading

def worker():
    """thread worker function"""
    print('Worker')


for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
