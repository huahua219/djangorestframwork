# python管道：Linux进程间通信方式的一种，管道有两端，读端和写端
"""
4.总结：
    1.向管道发送数据使用send函数，从管道接收数据使用recv()函数
    2.recv()函数为阻塞函数，当管道中数据为空的时候会阻塞
    3.一次recv()只能接收一次send()的内容
    4.send可以发送的数据类型比较多样，字符串，数字，列表等等
"""
import os
import time
from multiprocessing import Pipe
from multiprocessing.context import Process


def fun(name, a):
    time.sleep(1)
    # 字符串网管道里发送
    # a.send('huahau最帅'+ str(name))
    print('father id:', os.getppid(), "------", 'son id :', os.getpid())


if __name__ == '__main__':

    # 创建管道对象，管道函数返回2个对象
    child_conn, parent_conn = Pipe(duplex=False)
    job = []
    # 创建5个进程
    for  i in range(5):
        p = Process(target=fun, args=(i, child_conn))
        # 新的进程添加到列表里
        job.append(p)
        p.start()

    # 从管道中接收是，此时写在了join前面， 意味着这个for循环和所有的子进程同步进行
    for i in range(5):
        data = parent_conn.recv()
        print(data)

    for i in job:
        i.join()