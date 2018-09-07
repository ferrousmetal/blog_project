from django.urls import path
from article.views import *
app_name="article"

urlpatterns=[
    path('article-column/',article_column,name="article_column"),
]