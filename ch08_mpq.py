# ch08_mpq.py
def main():
    import multiprocessing
    workers = ['Alice', 'Bob']
    q = multiprocessing.Queue()
    pList = []
    for s in workers:
        p = multiprocessing.Process(target=f, args=(s, q))
        p.start()
        pList.append(p)
    for p in pList:
        p.join()
    print("="*20)
    while not q.empty():
        result = q.get()
        print( result )

def f(name, q):
    import time, random
    n = random.randint(2, 10)
    for i in range(n):
        time.sleep( 0.1 * random.randint(1, 5) )
        msg = "{} - {}/{}".format(name, i+1, n)
        print("Inserting", msg)
        q.put(msg)

if __name__ == "__main__":
        main()
