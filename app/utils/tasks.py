from __future__ import absolute_import


from config.celery import app


# worker 에서 say_hello 함수가 실행
@app.task
def say_hello():
    print('안녕하세요')

# Command
#   redis-server
#   celery -A config worker -l info
#   celery -A config beat -l info
