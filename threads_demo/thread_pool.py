"""
http://c.biancheng.net/view/2627.html

pool = ThreadPool(poolsize)
requests = makeRequests(some_callable, list_of_args, callback)
[pool.putRequest(req) for req in requests]
pool.wait()
"""

import time

import threadpool as threadpool


def sayhello(string):
    print("Hello ", string)
    time.sleep(2)


name_list = ['xiaozi', 'aa', 'bb', 'cc']
start_time = time.time()

pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()