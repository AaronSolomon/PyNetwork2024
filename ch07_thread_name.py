import threading
import time
def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')

def manager():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(3)
    print(threading.current_thread().getName(), 'Exiting')

s = threading.Thread(name='Manager', target=manager)
c = threading.Thread(name='worker', target=worker)
c2 = threading.Thread(target=worker)  # use default name

c.start()
c2.start()
s.start()
print(threading.current_thread().getName(), 'Exiting')
