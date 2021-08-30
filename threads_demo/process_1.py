import multiprocessing
import time


# def worker(interval):
#     n = 5
#     while n > 0:
#         print('the time is {}0'.format(time.ctime()))
#         time.sleep(interval)
#         n -= 1


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 0

if __name__ == '__main__':
    # p = multiprocessing.Process(target=worker, args=(3,))
    # p.start()
    pass



