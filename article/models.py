from django.db import models
from django.db.models import CASCADE
from django import forms

from user.models import User


class Article(models.Model):
    title = models.CharField('title', max_length=256)
    text = models.TextField('text')
    date_time = models.DateTimeField('datetime', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
