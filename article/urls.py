from django.urls import path

import article.views

urlpatterns = [
    path('', article.views.show_articles, name='index')
]
