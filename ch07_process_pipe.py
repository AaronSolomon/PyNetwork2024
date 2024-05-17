import multiprocessing

def worker(conn):
    conn.send(100)
    conn.send(200)
    conn.send(300)
    

a, b = multiprocessing.Pipe(duplex=False)
p = multiprocessing.Process(target=worker, args=(b,))
p.start()
p.join()

for i in range(3):
    n = a.recv()
    print(n)
