# ch07_process_names.py
import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    print('{} ({}) Starting'.format(name, pid))
    time.sleep(2)
    print('{} Exiting'.format(name))


def my_service():
    name = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    print('{} ({}) Starting'.format(name, pid))
    time.sleep(3)
    print('{} Exiting'.format(name))

if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name='worker 1',
        target=worker,
    )
    worker_2 = multiprocessing.Process(  
        target=worker,	 # default name
    )

    worker_1.start()
    worker_2.start()
    service.start()
