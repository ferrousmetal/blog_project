from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
    title=models.CharField(max_length=300,verbose_name="文章标题")
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE,verbose_name="作者")
    body=models.TextField(verbose_name="内容")
    publish=models.DateTimeField(default=timezone.now,verbose_name="发布时间")


    class Meta:
        verbose_name="文章"
        verbose_name_plural=verbose_name
        ordering=("-publish",)
    def __str__(self):
        return self.title
# Create your models here.
