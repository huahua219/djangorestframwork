

def test(num):
    in_num = num
    def nested(label):
        nonlocal in_num
        in_num += 1
        print(label, in_num)
    return nested

F = test(0)
print(F('a'))
print(F('b'))