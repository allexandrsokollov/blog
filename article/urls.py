from django.urls import path

import article.views

urlpatterns = [
    path('', article.views.show_articles, name='index'),
    path('newArticle/', article.views.new_article, name='newArticle'),
    path('addNewArticle', article.views.add_new_article, name='addNewArticle'),
    path('edit_article/<int:pk>', article.views.DetailArticle.as_view(), name='edit_article')
]
