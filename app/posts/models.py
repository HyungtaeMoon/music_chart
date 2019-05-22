from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.db import models


class BugsChart(models.Model):
    ranking = models.PositiveSmallIntegerField()
    image_file = models.ImageField(upload_to='bugs_album')
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '벅스뮤직'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    def __str__(self):
        return self.title
