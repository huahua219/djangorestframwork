####1.python面向对象学习（七）单例
    张风闲 2018-11-22 原文
    目录
    1. 单例设计模式
        单例设计模式的应用场景
    2. __new__ 方法
    3. Python 中的单例
        只执行一次初始化工作
        1. 单例设计模式
            设计模式
                设计模式 是 前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对 某一特定问题的成熟的解决方案
                使用 设计模式 是为了可重用代码、让代码更容易被他人理解、保证代码可靠性
            单例设计模式
                目的 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例
                每一次执行 类名() 返回的对象，内存地址是相同的
            单例设计模式的应用场景
                音乐播放 对象
                回收站 对象
                打印机 对象
    ……
####2. __new__ 方法
    使用 类名() 创建对象时，Python 的解释器 首先 会 调用 __new__ 方法为对象 分配空间
    __new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：
        在内存中为对象 分配空间
        返回 对象的引用
    Python 的解释器获得对象的 引用 后，将引用作为 第一个参数，传递给 __init__ 方法
    重写 __new__ 方法 的代码非常固定！
    
    重写 __new__ 方法 一定要 return super().__new__(cls)
    否则 Python 的解释器 得不到 分配了空间的 对象引用，就不会调用对象的初始化方法
    注意：__new__ 是一个静态方法，在调用时需要 主动传递 cls 参数

        class MusicPlayer(object):
            def __new__(cls, *args, **kwargs):
                print("执行__new__")
                instance = super().__new__(cls)
                return instance
            def __init__(self):
                print("执行__init__")
        mp1 = MusicPlayer()
        print(mp1)
####3. Python 中的单例
    单例 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例
    定义一个 类属性，初始值是 None，用于记录 单例对象的引用
    重写 __new__ 方法
    如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果
    返回 类属性 中记录的 对象引用
        class MusicPlayer(object):
            instance = None
            def __new__(cls, *args, **kwargs):
                if cls.instance is None:
                    cls.instance = super().__new__(cls)
                return cls.instance
        mp1 = MusicPlayer()
        print(mp1)
        mp2 = MusicPlayer()
        print(mp2)
    只执行一次初始化工作
        在每次使用 类名() 创建对象时，Python 的解释器都会自动调用两个方法：
        __new__ 分配空间
        __init__ 对象初始化
        在上一小节对 __new__ 方法改造之后，每次都会得到 第一次被创建对象的引用
        但是：初始化方法还会被再次调用

    需求:
        让 初始化动作 只被 执行一次
    解决办法:
        定义一个类属性 init_flag 标记是否 执行过初始化动作，初始值为 False
        在 __init__ 方法中，判断 init_flag，如果为 False 就执行初始化动作
        然后将 init_flag 设置为 True
        这样，再次 自动 调用 __init__ 方法时，初始化动作就不会被再次执行 了

            class MusicPlayer(object):
                instance = None
                init_flag = False
                def __new__(cls, *args, **kwargs):
                    if cls.instance is None:
                        cls.instance = super().__new__(cls)
                    return cls.instance
                def __init__(self):
                    if not MusicPlayer.init_flag:
                        print("初始化音乐播放器")
                        MusicPlayer.init_flag = True
            mp1 = MusicPlayer()
            print(mp1)
            mp2 = MusicPlayer()
            print(mp2)

####4.代码
    class Single(object):
    
        # instance = None
        flag = None
        def __new__(cls, *args, **kwargs):
            # if Single.instance is None:
                # obj = object.__new__(cls)
                # Single.instance = obj
    
                # cls.instance = super().__new__(cls)
            # return cls.instance
    
            if not hasattr(cls, 'instance'):
                cls.instance = super().__new__(cls)
            return cls.instance
    
        def __init__(self):
            if not Single.flag:
                print('create new obj')
                Single.flag = True
    
    s1 = Single()
    s2 = Single()
    print(id(s1))
    print(id(s2))
    print(s1.instance)
    print(s1.flag)
