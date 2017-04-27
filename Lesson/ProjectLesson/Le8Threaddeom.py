#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:Le8Threaddeom.py
@time:2017/4/26 21:26
"""
from threading import Thread, current_thread,Lock
import time

def worker(l):
    while True:
        l.acquire()
        print 'in worker %s' % current_thread()
        l.release()
        time.sleep(0.5)

class MyThread(Thread):
    def __init__(self,l):
        Thread.__init__(self)
        self._l=l

    def run(self):
        while True:
            self._l.acquire()
            print 'in worker %s' % current_thread()
            self._l.release()
            time.sleep(0.5)


if __name__=='__main__':
    l = Lock()
    print 'in main %s' % current_thread()
    #threads = [Thread(target=worker, args=[l]) for i in range(5)]
    threads = [MyThread(l) for i in range(5)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()