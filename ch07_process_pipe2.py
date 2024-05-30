import multiprocessing

def worker(conn, i):
    for j in range(1, 4):
        n = conn.recv()
        print(n)
    

a, b = multiprocessing.Pipe(duplex=False)
p = multiprocessing.Process(target=worker, args=(a,1))
p2 = multiprocessing.Process(target=worker, args=(a,2))
p.start()
p2.start()
for i in range(600):
    b.send(10*i)
p.join()
p2.join()

