from django.urls import path

import article.views

urlpatterns = [
    path('', article.views.show_articles, name='index'),
    path('newArticle/', article.views.new_article, name='newArticle'),
    path('addNewArticle', article.views.add_new_article, name='addNewArticle'),
    path('edit_article/<int:pk>', article.views.UpdateArticle.as_view(), name='edit_article'),
    path('delete_article/<int:pk>', article.views.DeleteArticle.as_view(), name='delete_article'),
    path('article/<int:pk>', article.views.ArticleDetailView.as_view(), name='article')
]
