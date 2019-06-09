from __future__ import absolute_import

from celery import shared_task

from crawling.bugs_crawling import get_ranking_chart


@shared_task
def task_for_crawling():
    # print('hello')
    get_ranking_chart()


# Command
#   redis-server
#   celery -A config worker -l info
#   celery -A config beat -l info
