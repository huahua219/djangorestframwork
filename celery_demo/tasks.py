from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker
# app = Celery('tasks', backend='redis://:yourpassword@localhost:6379/0', broker='redis://:yourpassword@localhost:6379/0')  # 配置好celery的backend和broker


@app.task  # 普通函数装饰为 celery task
def add(x, y):
    return x + y