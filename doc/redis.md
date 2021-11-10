####使用Homebrew安装命令
    brew install redis

####查看安装及配置文件位置
    Homebrew安装的软件会默认在/usr/local/Cellar/路径下
    redis的配置文件redis.conf存放在/usr/local/etc路径下

####启动redis服务
    方式一：使用brew帮助我们启动软件
    brew services start redis
    方式二
    redis-server /usr/local/etc/redis.conf
    执行以下命令
    redis-server

####redis-cli连接redis服务
    redis-cli -h 127.0.0.1 -p 6379

######关闭redis服务
    redis-cli shutdown

####强行终止redis
    sudo pkill redis-server

####基本操作命令
    显示所有key值： keys *
    设置值： set key value
    获取值： get key

    DBSIZE  key 数量
    flushdb 清空当前数据库中的所有 key
    flushall 清空所有数据库中的所有 key

