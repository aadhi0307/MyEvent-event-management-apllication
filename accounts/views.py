from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from adminapp import views
from accounts.models import admindb
from adminapp.views import indexpage


# Create your views here.
def adminlogin(req):
    return render(req,"login_signup.html")
def admindata(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        mb=req.POST.get('mobile')
        im=req.FILES['image']
        pswd = req.POST.get('pwd')
        cpswd = req.POST.get('cpwd')
        obj=admindb(name=na,email=em,mobile=mb,image=im,pwd=pswd,cpwd=cpswd)
        obj.save()
        messages.success(req, "Signup successfully")
        return redirect(adminlogin)
def adminsignin(req):
    if req.method=="POST":
        uname=req.POST.get('name')
        pwd=req.POST.get('pwd')
        if admindb.objects.filter(name=uname,pwd=pwd).exists():
            req.session['name']=uname
            req.session['pwd']=pwd
            messages.success(req, "Login successfully")
            return redirect(indexpage)
        else:
            messages.error(req, "incorrect username or password")
            return redirect(adminlogin)
    return redirect(adminlogin)
def adminlogout(req):
    del req.session['name']
    del req.session['pwd']
    return redirect(adminlogin)