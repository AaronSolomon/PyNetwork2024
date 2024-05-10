import threading, time, logging

def daemon():
    logging.info('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def non_daemon():
    logging.info('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s', )

d = threading.Thread(name='daemon', target=daemon, daemon=True)
n = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
n.start()
