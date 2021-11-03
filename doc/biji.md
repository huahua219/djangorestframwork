######1,
    列表作为栈使用：用append/pop，“后进先出”

    循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
    迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
    遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。
    递归（recursion），指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列。

    为什么要使用生成器？因为效率?
        使用生成器表达式取代列表推导式可以同时节省 cpu 和 内存(RAM)。
    https://blog.csdn.net/u014745194/article/details/70176117
    第一类：生成器函数
    第二类：生成器表达式：
        生成器是一类特殊的迭代器。

######3,定时器 Timer


######8,__getattr__()
    定义了__getattr__()，当访问object不存在的属性时会调用该方法
    不定义访问不存在的属性时会报 AttributeError
    class Cat(object):
        def __init__(self):
            self.name = "jn"

        def __getattr__(self, item):
            return "tm"

    cat = Cat()
    print(cat.name)
    print(getattr(cat, 'name'))
    print("*" * 20)
    print(cat.age)
    print(getattr(cat, 'age'))

######9,属性访问的优先级：(https://www.cnblogs.com/andy1031/p/10923834.html)
    __getattribute__ > __getattr__ > __dict__
    
    class Cat(object):

    def __init__(self):
        self.name = "China"

    def __getattr__(self, item):
        return "huaua"

    def __getattribute__(self, item):
        return 'girl'


    cat = Cat()
    print(cat.name)
    print(cat.age

######10, 装饰器
    https://blog.csdn.net/five3/article/details/83447467