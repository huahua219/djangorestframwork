""""
python数据结构： 堆栈 ，图， 链表，队列, 锁分配， 信号量加减， 状态管理， 数据库连接
"""
# from collections import Iterator
from collections import Counter

str = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
d = {"1":3, "3":2, "17":2}

# print ("Counter(s):", Counter(str))
# print ("Counter(li):", Counter(li))
# print ("Counter(d):", Counter(d))

d1 = Counter(str)
print(d1)
# print ("d1.most_common(2):",d1.most_common())
# print (d1.elements())

d2 = Counter(d)
print("若是字典的话返回value个key:", d2.elements())

#update和set集合的update一样，对集合进行并集更新
print (d1.update("sas1"))