from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate,login,logout
from account.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def register(request):
    if request.method=="POST":
        user_form=RegisterForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("成功")
        else:
            return HttpResponse("注册失败")
    else:
        user_form=RegisterForm()
        userprofile_form = UserProfileForm()
        return render(request,"account/register.html",{"form":user_form,"profile":userprofile_form})

@login_required(login_url='/account/login/')
def myelf(request):
    user=User.objects.get(username=request.user.username)
    userprofile=UserProfile.objects.get(user=user)
    userinfo=UserInfo.objects.get(user=user)
    return render(request,"account/myself.html",{"user":user,"userinfo":userinfo,"userprofile":userprofile})

@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth":userprofile.birth, "phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school, "company":userinfo.company, "profession":userinfo.profession, "address":userinfo.address, "aboutme":userinfo.aboutme})
        return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form, "userinfo_form":userinfo_form})

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method=="POST":
        img=request.POST["img"]
        print(img)
        userinfo=UserInfo.objects.get(user=request.user.id)
        userinfo.photo=img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request,'account/imagecrop.html')

# Create your views here.
