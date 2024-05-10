import threading

counter = 0     # Shared resource (counter)

lock = threading.Lock()

def worker():
    global counter
    # lock.acquire()
    try:
        for _ in range(100000):
            counter += 1
    finally:
        # lock.release()
        pass

# Create and start two worker threads
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
