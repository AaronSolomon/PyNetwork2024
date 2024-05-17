import multiprocessing

def worker():
    """worker function"""
    print('Worker')

for i in range(5):
    p = multiprocessing.Process(target=worker)
    p.start()
