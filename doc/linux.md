###### ps (process status)
    -A 列出所有的进程
    -w 显示加宽可以显示较多的资讯
    -au 显示较详细的资讯
    -aux 显示所有包含其他使用者的行程
###### 如何查看端口
    lsof -i:端口号 用于查看某一端口的占用情况，比如查看8000端口使用情况，lsof -i:8000
    netstat -tunlp |grep 端口号，用于查看指定的端口号的进程情况，如查看8000端口的情况，netstat -tunlp |grep 8000
###### 杀死进程
    杀死某个进程: kill -9 pid
    多个python程序在运行，想要全部结束的话:killall -9 python