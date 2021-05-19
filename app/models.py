from django.db import models

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    github = models.CharField('github', max_length=100, null=True, blank=True)
    programming = models.CharField('学習言語', max_length=100)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.title


class Production(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル')
    skill = models.CharField('スキル', max_length=100)
    github = models.CharField('github', max_length=100, null=True, blank=True)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateTimeField('作成日時')
    description = models.TextField('説明')

    def __str__(self):
        return self.title
