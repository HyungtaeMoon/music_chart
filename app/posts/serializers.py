from rest_framework import serializers

from .models import BugsChart


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugsChart
        fields = ('id', 'ranking', 'image_file', 'image_url', 'title', 'artist', 'album', 'created_at')
        read_only_Fields = ('id',)
