from django.shortcuts import render

# Create your views here.
from fabric.context_managers import cd
from fabric.decorators import roles
from fabric.tasks import execute

"""
http://www.fabfile.org/
几个常用的环境变量如下：
    user：可以通过设置env.user来指定Fabric建立SSH连接时使用的用户名（默认使用本地用户名）。
    password：用来显式设置默认连接或者在需要的时候提供sudo密码。如果没有设置密码或密码错误，Fabric将会提示你输入。
    passwords：密码字典，针对不同的机器设置密码。
    warn_only：布尔值，用来设置Fabric是否在检测到远程错误时退出。
    hosts：全局主机列表。
    roledefs：定义角色名和主机列表的映射字典。
"""


from fabric.operations import local, run
from fabric.state import env

# 示例一：

# 设置机器列表的，env被称为环境字典，用来配置一些运行环境相关的信息
env.hosts = ['192.168.1.100', '192.168.1.101']
env.user = 'user'
env.password = 'passwd'

#或者 用户直接写到hosts里
# env.hosts = ['user@192.168.1.100', 'user@192.168.1.101']
def task1(name):
    print('hello %s!' % name)
    local('ls -la')  # 本地命令
    # run('ls -la')  # 远程命令

def task2():
    print('good night')

# *****************************

# 示例二： https://zhuanlan.zhihu.com/p/104777654
# 对于不同的服务器想执行不同的任务
env.roledefs = {
    'dev': ['user1@10.216.224.65', 'user2@10.216.224.66'],
    'online': ['user3@45.33.108.82']
}

# host strings必须由username@host:port三部分构成，缺一不可，否则运行时还是会要求输入密码
env.passwords = {
    'user1@10.216.224.65:22': 'passwd1',
    'user2@10.216.224.66:22': 'passwd2',
    'user3@45.33.108.82:22': 'passwd3'
}

@roles('dev')
def taskA():
    with cd('/usr/local/webserver'):
        run('pwd')

@roles('online')
def taskB():
    run('pwd')

def task():
    execute(taskA)
    execute(taskB)