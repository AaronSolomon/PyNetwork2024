import multiprocessing

def worker(n):
    """worker function"""
    print('Worker:', n)

for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    p.start()
