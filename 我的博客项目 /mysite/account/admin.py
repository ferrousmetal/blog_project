from django.contrib import admin
from account.models import *
class AdminUserProfile(admin.ModelAdmin):
    list_display = ("user","birth","phone")
    list_filter = ("phone",)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user","school","company","profession","address","aboutme","photo")
    list_filter = ("school","company","profession")
admin.site.register(UserProfile,AdminUserProfile)
admin.site.register(UserInfo,UserInfoAdmin)

# Register your models here.
