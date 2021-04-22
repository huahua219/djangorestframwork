from django.shortcuts import render

# Create your views here.
from fabric.operations import local

print('I love you!')
def task1(name):
    print('hello %s!' % name)
    local('git pull')

def task2():
    print('good night')



from fabric.api import *
env.hosts = ['root@192.168.10.11:22']
def deploy():
    run('ls') # run()用于执行远程命令，local()执行本地命令
    # 执行后会提示你输入密码，输入密码即可