import multiprocessing
import logging

def worker():
    print('Doing some work')

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.WARNING)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
