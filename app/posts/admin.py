from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import BugsChart


@admin.register(BugsChart)
class BugsAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'photo_tag', 'title', 'artist', 'album']

    list_display_links = ['title', 'artist']

    def photo_tag(self, item):
        if item.image_file:
            return mark_safe('<img src={} style="width: 75px;"/>'.format(item.image_file.url))
        return None
