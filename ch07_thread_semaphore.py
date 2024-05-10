import threading, logging, time, random

def worker():
    sema.acquire()
    logging.info("Starting")
    time.sleep(random.randint(1, 10))
    logging.info("Exiting")
    sema.release()

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s', )

sema = threading.Semaphore(2)
for _ in range(5):
    threading.Thread(target=worker).start()
