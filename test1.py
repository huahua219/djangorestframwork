

class Animals():

    def __init__(self, *args, **kwargs):
        self.name = 'huahua'
        self.age = 29


class Dao(Animals):

    def __init__(self, sex, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sex = sex
        self.name='huangmingting'


if __name__ == '__main__':
    instance = Dao(sex='femal')
    print(instance.name)
    print(instance.age)
    print(instance.sex)