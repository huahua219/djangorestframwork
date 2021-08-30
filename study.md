共享锁, 互斥锁, 悲观所,乐观锁

###1，fabric库 是一个python包 是一个基于ssh的部署工具包，

    fabric是一个python包 是一个基于ssh的部署工具包;http://www.fabfile.org/
    lcd(dir): 进入本机某目录
    local(cmd): 本机上执行命令
    cd(dir): 进入服务器某目录
    run(cmd):服务器上执行命令
    https://zhuanlan.zhihu.com/p/104777654

###Django 管理并发操作之悲观锁即select_for_update [行级锁]
    对于后端的服务，有可能要承受很大的并发，比如火车票购买系统，后端服务需要准确的反应出剩余的票数。
    那么后端怎么处理并发呢？ select … for update 是数据库层面上专门用来解决并发取数据后再修改的场景的，
    # @transaction.atomic
    def test_sql():
        with transaction.atomic():
            menus = Role.objects.select_for_update().get(id=7)  # 行级锁
            menus.name = 'cccc'
            menus.save()
    所有匹配的行将被锁定，直到事务结束。这意味着可以通过锁防止数据被其它事务修改。
    一般情况下如果其他事务锁定了相关行，那么本查询将被阻塞，直到锁被释放。 如果这不想要使查询阻塞 的话，使用select_for_update(nowait=True)。 
    如果其它事务持有冲突的锁，互斥锁, 那么查询将引发 DatabaseError 异常。你也可以使用select_for_update(skip_locked=True)忽略锁定的行。 
    nowait和　　skip_locked是互斥的，同时设置会导致ValueError。
    目前，postgresql，oracle和mysql数据库后端支持select_for_update()。 但是，MySQL不支持nowait和skip_locked参数。
    使用不支持这些选项的数据库后端（如MySQL）将nowait=True或skip_locked=True转换为select_for_update()将导致抛出DatabaseError异常，这可以防止代码意外终止。


###django的F()原子操作:
        1:F()表达式:这种方法没有使用数据库中特定的原始的值，而是当 save() 执行时，让数据库去根据数据库当前的值进行更新操作;避免了并发时的安全问题
          from django.db.models import F
          product = Product.objects.get(name='huahua')
          product.numbe = F('num') + 1
          product.save()

        2: 可以实现一个模型中不同属性的运算操作
            models.Product.objects.update(price=F('price')+50)

        3:可以获取属性的值
            company = Company.objects.all() 
            companys = company.filter(c_boy_num__gt=F('c_girl_num'))   # 同一个模型查询男生比女生多的公司

### django原子性操作:
    try:
        with transaction.atomic():
            model.object.create(**kwargs)
    except:
        data = {'msg': 'error', 'code': 500 }
        
            
        