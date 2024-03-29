# 定义一个准备作为线程任务的函数
import threading
from concurrent.futures.thread import ThreadPoolExecutor

# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum

# 创建一个包含2条线程的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action, 50)
    # 向线程池再提交一个task, 100会作为action()函数的参数
    future2 = pool.submit(action, 100)
    def get_result(future):
        print(future.result())
    # 为future1添加线程完成的回调函数
    future1.add_done_callback(get_result)
    # 为future2添加线程完成的回调函数
    future2.add_done_callback(get_result)
    print('--------------')


# 创建一个包含4条线程的线程池
# with ThreadPoolExecutor(max_workers=4) as pool:
#     # 使用线程执行map计算
#     # 后面元组有3个元素，因此程序启动3条线程来执行action函数
#     results = pool.map(action, (50, 100, 150))
#     print('--------------')
#     for r in results:
#         print(r)