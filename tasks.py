import time
from celery import Celery

app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='db+sqlite:///db.sqlite'
)


@app.task
def add(x, y):
    time.sleep(10)
    return x + y
