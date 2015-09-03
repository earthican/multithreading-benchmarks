#!/usr/bin/python

import Queue
import threading
import time

def num_stringify(num):
    return ''.join([(c + ',') if i % 3 == 0 and i > 0 else c for i, c in enumerate(str(num)[::-1])][::-1])

def main():
    count = 0
    start = time.time()
    for i in range(1, int(1e8)+1):
        count += 1
    end = time.time()


    print'''
        # iterations: {count}
        Time elapsed: {time}
    '''.format(count=num_stringify(count), time=time.strftime('%H:%M:%S', time.gmtime(end-start)))

if __name__ == '__main__':
    main()
