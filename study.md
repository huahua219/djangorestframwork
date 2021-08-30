###1，fabric库 是一个python包 是一个基于ssh的部署工具包，

    fabric是一个python包 是一个基于ssh的部署工具包;http://www.fabfile.org/
    lcd(dir): 进入本机某目录
    local(cmd): 本机上执行命令
    cd(dir): 进入服务器某目录
    run(cmd):服务器上执行命令
    https://zhuanlan.zhihu.com/p/104777654


###悲观锁：
    1，悲观锁包括：共享锁（读锁）， 排它锁（写锁）
    2，要使用悲观锁，必须关闭 MySQL 数据库的自动提交属性set autocommit=0。因为 MySQL 默认使用 autocommit 模式，也就是说，当执行一个更新操作后，MySQL 会立刻将结果进行提交。
    3,使用 select…for update 锁数据，需要注意锁的级别，MySQL InnoDB 默认行级锁。行级锁都是基于索引的，如果一条 SQL 语句用不到索引是不会使用行级锁的，会使用表级锁把整张表锁住，这点需要注意。