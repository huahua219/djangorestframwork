"""
Python 线程安全（同步锁Lock）：银行取钱
"""

import threading
import time


class Acount(object):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance
        self.lock = threading.RLock()

    def getBalance(self):
        return self.__balance

    def draw(self, draw_account):
        self.lock.acquire()
        try:
            if self.__balance >= draw_account:
                print(threading.currentThread().name + '吐钱成功' + str(draw_account))

                time.sleep(1)
                self.__balance -= draw_account
                print('余额为：'+ str(self.__balance))
            else:
                print(threading.currentThread().name + '取钱失败！余额不足')
        finally:
            self.lock.release()


def draw(account, draw_account):
    account.draw(draw_account)

acct = Acount('1234567', 11000)

threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 600)).start()
threading.Thread(name='丙', target=draw, args=(acct, 200)).start()
threading.Thread(name='丁', target=draw, args=(acct, 100)).start()




