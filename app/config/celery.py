import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab


# Django 의 세팅 모듈을 Celery 의 기본으로 사용하도록 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

# app 인스턴스 객체 생성
app = Celery(
    'config',
)

# 문자열로 등록한 이유는 Celery Worker 가 자식 프로세스에
# configuration object 를 직렬화하지 않아도 된다는 것 때문
# namespace = 'CELERY'는 모든 celery 관련한 configuration key 가
# 'CELERY_' 로 시작해야함을 의미함
app.config_from_object('django.conf:settings', namespace='CELERY')

# task 모듈을 모든 등록된 Django App config 에 load 함
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-minute-crontab': {
        'task': 'utils.tasks.task_for_crawling',
        'schedule': crontab(),  # 1분마다
        'args': (),
    },
}


# bing=True 옵션을 주게 되면
# 아래 함수의 인자에 self 가 추가됨 ==> 'self'는 관용적으로 쓰임
# 이 앱을 실행시켰을 때의 대한 정보가 담겨져옴

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
