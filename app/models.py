from django.db import models


class Post(models.Model):
    """記事"""
    title = models.CharField('タイトル', max_length=32)
    text = models.TextField('本文')
    relation_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)

    def __str__(self):
        return self.title
