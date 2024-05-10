import threading ,time ,logging

def worker():
    time.sleep(5)

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker)
    t.start()

main_thread = threading.main_thread()
logging.debug(main_thread.getName())

for t in threading.enumerate(): 
    if t is not main_thread:		# The list includes the current thread (main thread)
        logging.debug(t.getName())
