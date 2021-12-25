####数据5大框架：主流大数据框架对比分析
    https://zhuanlan.zhihu.com/p/108826825
    https://www.cnblogs.com/oc-bowen/p/6109009.html
####容器博客
    http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html
####C语言博客
    https://www.ruanyifeng.com/blog/2021/09/c-language-tutorial.html
####ssh博客
    https://wangdoc.com/ssh/port-forwarding.html
####linux内核：
    https://www.kernel.org/doc/html/latest/translations/zh_CN/kernel-hacking/index.html


https://hub.docker.com/search?type=image
https://docs.docker.com/get-docker/

#####查看docker服务状态(root用户使用):
    systemctl status docker

####启动docker服务
    sudo service docker start
    sudo systemctl start docker

####命令的用法
    查看进行中容器 docker ps
    查看进行中所有容器 docker ps -a  或（docker container ls -a）
    查看镜像：docker image ls 或 docker images
    获取镜像：docker pull 镜像名
    删除镜像：docker rmi [image]   
            docker image rm [image]
    从镜像启动容器：docker run -it ubuntu /bin/bash
        参数说明：
            -i: 交互式操作。
            -t: 终端。
            -P:将容器内部使用的网络端口随机映射到我们使用的主机上。
            ubuntu: ubuntu 镜像。
            /bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。

    启动容器后台运行:docker run -itd --name ubuntu-test ubuntu /bin/bash
        参数说明：
            -d 参数默认不会进入容器(让容器在后台运行)

    启动一个已停止的容器：docker start <容器 ID>
    重启停止的容器:docker restart <容器 ID>
    进入容器:
        docker attach <容器 ID> 
        docker exec -it <容器 ID> bash
    退出(容器会停止)：exit
    退出(容器会不会停止)docker exec -it <容器 ID> 

    导出容器:ocker export <容器 ID> >  fileName<本地路径>
    导入容器快照:
    删除容器：docker rm -f <容器 ID> 
    清理掉所有处于终止状态的容器：docker container prune
    查看 WEB 应用程序log日志:docker logs -f <容器 ID/名字>
    搜索镜像：docker search 名字

    
    docker rmi [images ID]  # 删除此 ID 的镜像
    docker container stop [container ID]  # 停止此 ID 的容器
    docker container start [container ID]  # 启动此 ID 的容器
    docker container rm [container ID]  # 删除此 ID 的容器
    运行容器：
        docker run -p 7979:7979 6811c43789de
  

####dockerfile构建镜像开启容器
    docker build命令中使用-f标志指向文件系统中任何位置的Dockerfile。
    构建容器：sudo docker build .  -t python:3.6 

####docker-compose
    确认 docker-compose 是否安装成功：docker-compose -v
