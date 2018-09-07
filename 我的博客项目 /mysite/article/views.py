from django.shortcuts import render
from article.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/login/")
def article_column(request):
    columns=ArticleColumn.objects.filter(user=request.user)
    return render(request,"article/column/article_column.html",{"columns":columns})
# Create your views here.
