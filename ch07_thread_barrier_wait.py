import threading, logging, time

logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)

def worker():
    n = b.wait()
    logging.info("Still {} threads haven't passed the barrier.".format(n))
    if n == 0:
        time.sleep(0.1)
        logging.info("I am the last one.")

b = threading.Barrier(5)
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
