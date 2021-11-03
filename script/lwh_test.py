# yield语法也是Python中比较有特点的语法糖，可以说是特有的。虽然其它语言有实现类似机制的功能。 yield是Python中实现**协程(coroutine)**的一个重要基础

# 重要的往往在最后面，装饰器是学习Python绕不过去的坎。就像学习Java要理解面向对象和设计模式一样。 学习Python，你就应该要掌握好闭包、生成器、装饰器等相关知识。而对于编写高并发程序时则要掌握协程相关知识。
from multiprocessing import Pool
from multiprocessing.context import Process


def f(x):
    return x*x

def p1():
    with Pool(5) as p:
        res = p.map(f, [1, 2, 3])
        print(res)
    return res

def p2():
    p = Process()

if __name__ == '__main__':
    p1()