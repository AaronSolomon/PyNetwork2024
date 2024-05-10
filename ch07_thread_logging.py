import logging, threading, time

def worker():
    logging.info('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def manager():
    logging.info('Starting')
    time.sleep(3)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

s = threading.Thread(name='Manager', target=manager)
c = threading.Thread(name='Worker', target=worker)
c2 = threading.Thread(target=worker)  # use default name

c.start()
c2.start()
s.start()
logging.debug('Exiting')
