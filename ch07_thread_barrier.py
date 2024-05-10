import threading, logging, random, time

logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)

def worker():
    i = random.randint(2, 10)
    logging.info(f"Waiting {i} seconds")
    time.sleep(i)
    # b.wait()
    logging.info("Exiting")

b = threading.Barrier(5)
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
