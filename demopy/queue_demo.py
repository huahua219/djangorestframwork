"""
在Python中，队列是最常用的线程间的通信方法，因为它是线程安全的，自带锁。而Condition等需要额外加锁的代码操作，在编程对死锁现象要很小心，Queue就不用担心这个问题。
"""
from collections import deque
from queue import Queue, LifoQueue, PriorityQueue
import time, threading


# 常用队列方法：
def fun_queue():
    # 先进先出队列
    q = Queue(maxsize=5)
    # 后进先出队列
    lq = LifoQueue(maxsize=6)
    # 优先级队列
    pq = PriorityQueue(maxsize=5)

    for i in range(10,15):
        q.put(i)
        lq.put(i)
        pq.put(i)

    print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
    print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
    print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))
    print(q.get(), lq.get(), pq.get())
    print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
    print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
    print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))

# 双边队列
def doule_queue():
    dq = deque(['a', 'b'])
    dq.append('c')
    print(dq)
    print(dq.pop())
    print(dq)
    print(dq.popleft())
    print(dq)
    dq.appendleft('d')
    print(dq)
    print(len(dq))


# 采用生产者消费者模式开发的Python多线程
def consume_production():
    q = Queue(maxsize=0)

    def product(name):
        count = 1
        while True:
            q.put('气球兵{}'.format(count))
            print('{}训练气球兵{}只'.format(name, count))
            count += 1
            time.sleep(5)

    def consume(name):
        while True:
            print('{}使用了{}'.format(name, q.get()))
            time.sleep(1)
            q.task_done()

    t1 = threading.Thread(target=product, args=('wpp',))
    t2 = threading.Thread(target=consume, args=('ypp',))
    t3 = threading.Thread(target=consume, args=('others',))

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    consume_production()