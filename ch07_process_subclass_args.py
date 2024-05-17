import multiprocessing

class Worker(multiprocessing.Process):

    def __init__(self, n):
        multiprocessing.Process.__init__(self)
        self.n = n
    def run(self):
        print('In Worker-{}'.format(self.n))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker(i)
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
