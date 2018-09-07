from django.urls import path
from blog.views import *

app_name="blog"
urlpatterns=[
    path("",blog_title,name="blog_title"),
    path("content/<article_id>/",blog_article,name="blog_detail"),


]