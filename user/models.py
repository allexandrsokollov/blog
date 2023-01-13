from django.db import models


class User(models.Model):
    name = models.CharField('name', max_length=64)
    login = models.CharField('login', max_length=64)
    password = models.CharField('password', max_length=64)

    def __str__(self):
        return 'name: ' + self.name + ' login: ' + self.login

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
