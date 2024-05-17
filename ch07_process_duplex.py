import multiprocessing

def worker(conn):
    conn.send(100)
    conn.send(200)
    conn.send(300)
    result = conn.recv()
    print(result)


a, b = multiprocessing.Pipe(duplex=True)
p = multiprocessing.Process(target=worker, args=(b,))
p.start()

sum = 0
for i in range(3):
    n = a.recv()
    sum += n
a.send(sum)
