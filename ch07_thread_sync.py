import threading, time, logging

def worker():
    logging.info('Starting')
    time.sleep(2)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s', )

t1 = threading.Thread(target=worker)

logging.info('Starting')
t1.start()
# Synchronization
logging.debug('Waiting for Thread-1')
# t1.join()		# This holds (blocks) the calling thread until t1 is terminated.
logging.debug('Exiting')

