#!/usr/bin/python

import Queue
import threading
import time

NUM_ELEMENTS = int(1e2)
NUM_THREADS = 8

def num_stringify(num):
    return ''.join([(c + ',') if i % 3 == 0 and i > 0 else c for i, c in enumerate(str(num)[::-1])][::-1])

def single_thread():
    count = 0
    start = time.time()
    for i in range(1, NUM_ELEMENTS+1):
        count += 1
    end = time.time()

    print'''
        # iterations: {count}
        Time elapsed: {time}
    '''.format(count=num_stringify(count), time=time.strftime('%H:%M:%S', time.gmtime(end-start)))

COUNT = 0
COUNT_ELEMENTS = NUM_ELEMENTS
LOCK = threading.Lock()
class CounterThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        global COUNT_ELEMENTS
        global COUNT
        while COUNT_ELEMENTS > 0:
            LOCK.acquire()
            COUNT += 1
            COUNT_ELEMENTS -= 1
            LOCK.release()

def multithread():
    threads = []
    thread_id = 1
    start = time.time()
    for _ in range(NUM_THREADS):
        thread = CounterThread(thread_id)
        thread.start()
        threads.append(thread)
        thread_id += 1
    for thread in threads:
        thread.join()
    end = time.time()

    print'''
        # iterations: {count}
        Time elapsed: {time}
    '''.format(count=num_stringify(COUNT), time=time.strftime('%H:%M:%S', time.gmtime(end-start)))


if __name__ == '__main__':
    single_thread()
    multithread()
