def upper_attr(class_name, class_parents, class_attr):
    # class_name 会保存类的名字 Foo
    # class_parents 会保存类的父类 object
    # class_attr 会以字典的方式保存所有的类属性
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'

# print("check Foo exist bar attr=", hasattr(Foo, 'bar'))
# print("check Foo exist BAR attr=", hasattr(Foo, 'BAR'))

# *****************************************
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

# s1 = Single()
# s2 = Single()
# print(id(s1))
# print(id(s2))
# print(s1.instance)
# print(s1.flag)
# *****************************************