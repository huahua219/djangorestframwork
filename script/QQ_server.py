"""
https://blog.csdn.net/qq_33196814/article/details/80023790
https://blog.csdn.net/weixin_44100850/article/details/89512481
https://www.cnblogs.com/dalaoban/p/9331113.html
https://www.baidu.com/s?wd=python%20udp%E9%80%9A%E4%BF%A1&rsv_spt=1&rsv_iqid=0xfb0eb7d600000d46&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ts_1&rsv_btype=t&inputT=19611&rsv_t=e6c6R4mbDWPsPlvdAJhI5IHMyCBb1nW4ctF1xavctFvC%2Bg98vkii2dkJCPZ5x0kdeF69&rsv_sug3=59&rsv_sug1=69&rsv_sug7=100&oq=%25E5%25BE%25AE%25E4%25BF%25A1%25E8%2581%258A%25E5%25A4%25A9%25E5%25BA%2595%25E5%25B1%2582%25E5%258E%259F%25E7%2590%2586&rsv_pq=e91e22a90005ed8c&rsv_sug2=0&prefixsug=python%2520udp&rsp=1&rsv_sug4=20014
"""

from socket import socket


def main():
    # 创建套接字对象并指定使用哪种传输服务 socket()括号不传递参数默认是tcpipv4
    server = socket()
    # 绑定ip地址和端口(这样可以区分不同的服务) 端口可以自己指定建议使用1024以后的端口
    server.bind(('localhost', 5650))
    server.listen(512)    #开始监听 表示可以使用512个链接排队
    # 检查服务器是否已经启动
    print('服务器已启动')
    while True:
        # 接收客户端的连接  accpet是一个阻塞的方法  如果没有客户端连接到服务器,这个方法就会阻塞代码不会向下执行(返回的对象是一个元祖)
        client, addr = server.accept()
        print(str(addr) + '已经成功连接到服务器.')
        while True:
            recerver = client.recv(1024).decode('utf-8')
            if recerver:
                print(recerver)
            data = input('服务器:')
            client.send(data.encode('utf-8'))

        client.close()


if __name__ == '__main__':
    main()