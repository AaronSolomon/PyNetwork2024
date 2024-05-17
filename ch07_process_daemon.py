import multiprocessing
import time

def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    time.sleep(12)
    print('Exiting :', p.name, p.pid)

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    time.sleep(6)
    print('Exiting :', p.name, p.pid)

if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    n.start()
    time.sleep(5)
    print("MainProcess Exiting", \
       multiprocessing.current_process().pid)
