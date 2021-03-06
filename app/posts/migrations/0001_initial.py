# Generated by Django 2.2.1 on 2019-05-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugsChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveSmallIntegerField()),
                ('image_file', models.ImageField(upload_to='bugs_album')),
                ('image_url', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '벅스뮤직',
                'verbose_name_plural': '벅스뮤직 목록',
                'ordering': ['-pk'],
            },
        ),
    ]
