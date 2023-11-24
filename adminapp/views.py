from django.shortcuts import render,redirect
from adminapp.models import Category,Service,admindata
from userapp.models import Contactdata,booking
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

def indexpage(req):
    data=Category.objects.all()
    return render(req,"index.html",{"data":data})
def service_add(req):
    data = Category.objects.all()
    return render(req,"service_add.html", {"data":data})
def service_data(req):
    if req.method == "POST": 
        sn = req.POST.get('c_name')
        cn = req.POST.get('comp_name')
        im = req.FILES['comp_image']
        ds = req.POST.get('comp_description')
        ad = req.POST.get('comp_address')
        rn = req.POST.get('comp_rent')
        obj=Service(s_name=sn,service_name=cn,service_image=im,service_description=ds,service_address=ad,service_rent=rn)
        obj.save()
        return redirect(service_add)
    
def service_display(req):
    data=Service.objects.all()
    return render(req,"service_display.html",{"data":data})
def service_edit(req,dataid):
    data=Category.objects.all()
    serv=Service.objects.get(id=dataid)
    return render(req,"service_edit.html",{"data":data,"serv":serv})
def service_update(req,dataid):
    if req.method=="POST":
        sn = req.POST.get('c_name')
        cn = req.POST.get('comp_name')
        ds = req.POST.get('comp_description')
        ad = req.POST.get('comp_address')
        rn = req.POST.get('comp_rent')
        try:
            im=req.FILES['comp_image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Service.objects.get(id=dataid).service_image
    Service.objects.filter(id=dataid).update(s_name=sn,service_name=cn,service_image=file,service_address=ad,service_rent=rn,service_description=ds)
    return redirect(service_display)

def service_delete(req,dataid):
    serv=Service.objects.filter(id=dataid)
    serv.delete()
    return redirect(service_display)

def category_add(req):
    return render(req,"categoryadd.html")
def category_data(req):
    if req.method=="POST":
        cn=req.POST.get("category_name")
        im=req.FILES['category_image']
        ds=req.POST.get("category_description")
        obj=Category(name=cn,logo=im,description=ds)
        obj.save()
        return redirect(category_add)
def category_display(req):
    data=Category.objects.all()
    return render(req,"categorydisplay.html",{"data":data})
def category_edit(req,dataid):
    data=Category.objects.get(id=dataid)
    return render(req,"categoryedit.html",{"data":data})
def category_update(req,dataid):
    if req.method=="POST":
        cn=req.POST.get("category_name")
        ds=req.POST.get("category_description")
        try:
            im=req.FILES['category_image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Category.objects.get(id=dataid).logo
    Category.objects.filter(id=dataid).update(logo=file,name=cn,description=ds)
    return redirect(category_display)
def category_delete(req,dataid):
    data=Category.objects.filter(id=dataid)
    data.delete()
    return redirect(category_display)
def contact_display(req):
    data=Contactdata.objects.all()
    return render(req,"contactusdisplay.html",{"data":data})
def bookings(req):
    data=booking.objects.all()
    return render(req,"bookingdisplay.html",{"data":data})
def booking_delete(req,dataid):
    data=booking.objects.filter(id=dataid)
    data.delete()
    return redirect(bookings)
def admin_signin(req):
    return render(req,"admin_login.html")
def admin_data(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        mb=req.POST.get('mobile')
        pswd = req.POST.get('pwd')
        cpswd = req.POST.get('cpwd')
        obj=admindata(name=na,email=em,mobile=mb,pwd=pswd,cpwd=cpswd)
        obj.save()
        messages.success(req, "Signup successfully")
        return redirect(admin_signin)
def admin_login(req):
    if req.method=="POST":
        uname=req.POST.get('name')
        pwd=req.POST.get('pwd')
        if admindata.objects.filter(name=uname,pwd=pwd).exists():
            req.session['name']=uname
            req.session['pwd']=pwd
            messages.success(req, "Login successfully")
            return redirect(indexpage)
        else:
            messages.error(req, "incorrect username or password")
            return redirect(admin_login)
    return redirect(admin_login)

def admin_logout(req):
    del req.session['name']
    del req.session['pwd']
    return redirect(admin_signin)