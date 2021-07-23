####1分布式任务调度系统
    1，Celery 专注于实时任务处理，支持任务调度
    2，它是一个分布式队列的管理工具，我们可以用 Celery 提供的接口快速实现并管理一个分布式的任务队列。
    3，我们要理解 Celery 本身不是任务队列，它是管理分布式任务队列的工具，或者换一种说法，它封装好了操作常见任务队列的各种操作，我们用它可以快速进行任务队列的使用与管理

####Brokers
    brokers 中文意思为中间人，在这里就是指任务队列本身，Celery 扮演生产者和消费者的角色，brokers 就是生产者和消费者存放/拿取产品的地方(队列)
    常见的 brokers 有 rabbitmq、redis、Zookeeper 等

####Result Stores / backend
    顾名思义就是结果储存的地方，队列中的任务运行完后的结果或者状态需要被任务发送者知道，那么就需要一个地方储存这些结果，就是 Result Stores 了
    常见的 backend 有 redis、Memcached 甚至常用的数据都可以。

####Workers
    就是 Celery 中的工作者，类似与生产/消费模型中的消费者，其从队列中取出任务并执行

####Tasks
    就是我们想在队列中进行的任务咯，一般由用户、触发器或其他操作将任务入队，然后交由 workers 进行处理。


###启动命令
    celery -A tasks worker  --loglevel=info
    tasks为人物脚本tasks.py

####celery()参数解释
    tasks	为当前模块的名称,这个用来自动的获取在 main\ module中的任务
    main	如果作为__main__运行，则为主模块的名称。用作自动生成的任务名称的前缀
    loader	当前加载器实例
    backend	任务结果url
    amqp	AMQP对象或类名，一般不管
    log	日志对象或类名
    set_as_current	将本实例设为全局当前应用
    tasks	任务注册表。
    broker	使用的默认代理的URL,任务队列；
    include	每个worker应该导入的模块列表，以实例创建的模块的目录作为起始路径