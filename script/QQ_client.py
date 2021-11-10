import datetime
from socket import socket


def main():
    # 创建套接字对象
    client = socket()
    # 连接服务器
    client.connect(('localhost', 5650))
    while True:
        receiver = client.recv(1024).decode('utf-8')
        if receiver:
            print(receiver)

        data = input('客户端%s:' % datetime.datetime.now('%Y-%m-%d %H:%M:%S'))
        client.send(data.encode('utf-8'))  # 向服务端发送消息


    client.colse()


if __name__ == '__main__':
    main()
