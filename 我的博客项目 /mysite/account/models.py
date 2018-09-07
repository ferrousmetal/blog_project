from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE,verbose_name="用户")
    birth=models.DateField(blank=True,null=True,verbose_name="出生日期")
    phone=models.CharField(max_length=20,null=True,verbose_name="电话号码")

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return "user{}".format(self.user.username)
# Create your models here.

class UserInfo(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    school=models.CharField(max_length=100,blank=True)
    company=models.CharField(max_length=100,blank=True)
    profession=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=100,blank=True)
    aboutme=models.TextField(blank=True)
    photo=models.ImageField(blank=True)
    class Meta:
        verbose_name="注册信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.user.username