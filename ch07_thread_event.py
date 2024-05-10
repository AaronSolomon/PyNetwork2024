import threading, time, logging, random

def worker():
    n = random.randint(3, 8)
    logging.info(f"I need {n} seconds.")
    time.sleep(n)
    logging.info("I am ready")
    ready.set()

logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)

ready = threading.Event()
logging.info("Tell me when you are ready.")
t = threading.Thread(target=worker)
t.start()
ready.wait()
logging.info("OK")
