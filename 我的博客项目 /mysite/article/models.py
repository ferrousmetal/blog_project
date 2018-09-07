from django.db import models
from django.contrib.auth.models import User

class ArticleColumn(models.Model):
    user=models.ForeignKey(User,related_name="article_column",on_delete=models.CASCADE)
    column=models.CharField(max_length=200)
    created=models.DateField(auto_now_add=True)
    def __ster__(self):
        return self.user
    class Meta:
        verbose_name="文章字段"
        verbose_name_plural=verbose_name

# Create your models here.
