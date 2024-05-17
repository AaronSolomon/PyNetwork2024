import threading, multiprocessing

def worker(aList, n):
    aList.append(n)

tList = []
threads = []
for i in [1, 3, 5, 7]:
    t = threading.Thread(target=worker, args=(tList, i))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(tList)

pList = []
procs = []
for i in [1, 3, 5, 7]:
    p = multiprocessing.Process(target=worker, args=(pList, i))
    p.start()
    procs.append(p)
for p in procs:
    p.join()
print(pList)
