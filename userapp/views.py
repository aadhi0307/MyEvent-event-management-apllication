from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import Category,Service
from userapp.models import Userdata,Contactdata,Feedback,booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models import Q


# Create your views here.
def home(req):
    data=Category.objects.all()
    feed=Feedback.objects.all()
    return render(req,"home.html",{"data":data,"feed":feed})


def service(req, ser_name):
    data = Category.objects.all()
    
    if 'search' in req.GET:
        search_query = req.GET['search']
        ser = Service.objects.filter(Q(service_name__icontains=search_query))
        abc = Category.objects.none()  # No categories for search results
    else:
        ser = Service.objects.filter(s_name=ser_name)
        abc = Category.objects.filter(name=ser_name)
    
    return render(req, 'service.html', {"data": data, "ser": ser, "abc": abc})




 
def contactUs(req):
    user=Userdata.objects.all()
    data = Category.objects.all()
    return render(req,"contactus.html",{"data":data,"user":user})
def contactdata(req):
    if req.method=="POST":
        na=req.POST.get('username')
        em=req.POST.get('email')
        sb=req.POST.get('subject')
        mg=req.POST.get('message')
        obj=Contactdata(name=na,email=em,subject=sb,message=mg)
        obj.save()
        return redirect(contactUs)

def about(req):
    data = Category.objects.all()
    return render(req,"aboutus.html",{"data":data})
def bookingpage(req,id):
    user=Userdata.objects.all()
    data=Category.objects.all()
    b_data=Service.objects.filter(id=id)
    return render(req,"bookingpage.html",{"data":data,"user":user,"b_data":b_data})
def bookdata(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        dt=req.POST.get('date')
        rn=req.POST.get('rent')
        sn=req.POST.get('service')
        mg=req.POST.get('message')
        obj=booking(book_name=na,book_email=em,book_date=dt,book_rent=rn,book_service=sn,book_message=mg)
        obj.save()
        return redirect(invoice_view, booking_id=obj.id)  # Redirect to invoice view

    return redirect('home')

def invoice_view(req, booking_id):
    booking_instance = get_object_or_404(booking, id=booking_id)
    return render(req, 'invoice.html', {'booking': booking_instance})

def servicedetails(req,id):
    data=Category.objects.all()
    ser = Service.objects.filter(id=id)
    feedbacks = Feedback.objects.filter(select_service=ser.first().service_name)
    return render(req,"singlepage.html",{"data":data,'ser':ser,"feedbacks":feedbacks})
    

def feedback(req):
    if req.method=='POST':
        un=req.POST.get('user')
        fd=req.POST.get('feedback')
        sn=req.POST.get('serv')
        obj=Feedback(username=un,feedbacks=fd,select_service=sn)
        obj.save()
        return redirect(home)
    
def loginpage(req):
    return render(req,"loginpage.html")
def logindata(req):
    if req.method == "POST" :
        un=req.POST.get("uname")
        em=req.POST.get("email")
        pwd=req.POST.get("pwd")
        obj=Userdata(username=un,email=em,pwd=pwd)
        obj.save()
        return redirect(loginpage)
def user_login(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        pwd=req.POST.get('pwd')
        if Userdata.objects.filter(username=un,pwd=pwd).exists():
            req.session['uname']=un
            req.session['pwd']=pwd
            return redirect(home)
        else:
            return redirect(user_login)
    return redirect(user_login)

def user_logout(req):
    del req.session['uname']
    del req.session['pwd']
    return redirect(loginpage)



