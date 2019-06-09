import os

from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import requests
from bs4 import BeautifulSoup

from posts.models import BugsChart


def get_ranking_chart():
    pre_obj_items = BugsChart.objects.all()
    for pre_obj in pre_obj_items:
        print(f'{pre_obj} 객체를 acitve=False 처리합니다.')
        pre_obj.active = False
        pre_obj.save()

    chart_url = 'https://music.bugs.co.kr/chart'

    headers = {
        'User_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
    }
    req = requests.get(chart_url, headers=headers)
    html = req.text

    # file_name = 'bugs_chart_100.text'
    # with open('bugs_chart_100.text', 'wt') as f:
    #     f.write(html)

    soup = BeautifulSoup(html, 'html.parser')
    chart_table = soup.select('table tbody tr')
    for items in chart_table:
        try:
            ranking = items.select_one('div.ranking strong').get_text(strip=True)
            image_url = items.select_one('a.thumbnail img').get('src')
#             arrow = items.select_one('p.change span')
            title = items.select_one('th p.title a').get_text(strip=True)
            artist = items.select_one('p.artist a').get_text(strip=True)
            album = items.select_one('a.album').get_text(strip=True)
        except AttributeError:
            break
        print('앨범 이미지: {}'.format(image_url))

        print('순위: {} | 제목: {} | 아티스트: {} | 앨범: {}'.format(ranking, title, artist, album))

        response = requests.get(image_url, stream=True)
        image_name = os.path.basename(image_url.split('?', 1)[0])

        print(image_name)

        chart = BugsChart(
            ranking=ranking,
            image_url=image_url,
            title=title,
            artist=artist,
            album=album
        )
        chart.image_file.save(image_name, File(response.raw))
        chart.save()
    print('크롤링 완료!!!!')


if __name__ == "__main__":
    get_ranking_chart()
