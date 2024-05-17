import multiprocessing

def dot():
    import time, sys
    while True:
        time.sleep(1)
        print('.', end='')
        sys.stdout.flush()

p = multiprocessing.Process(target=dot)
p.start()
input("Please press <ENTER> ")
p.terminate()
p.join()
