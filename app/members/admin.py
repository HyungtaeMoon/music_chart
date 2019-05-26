from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class BugsAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'alias', 'profile', 'is_staff']

    list_display_links = ['email', 'name']

    readonly_fields = ['is_staff']

    def profile(self, user):
        if user.profile_img:
            return mark_safe('<img src={} style="width: 75px;"/>'.format(user.profile_img.url))
        return None
