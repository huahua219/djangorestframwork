import time

from tasks import fun_add


"""
delay 返回的是一个 AsyncResult 对象，里面存的就是一个异步的结果，当任务完成时result.ready() 为 true，然后用 result.get() 取结果即可
"""
result = fun_add.delay(4, 222)     #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(1)

print('task done: {0}'.format(result.get()))