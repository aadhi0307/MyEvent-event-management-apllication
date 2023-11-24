from django.urls import path
from userapp import views

urlpatterns = [
     path('home/',views.home,name="home"),
     path('service/<ser_name>/',views.service,name="service"),
     path('contactUs/',views.contactUs,name="contactUs"),
     path('contactdata/',views.contactdata,name="contactdata"),
     path('about/',views.about,name="about"),
     path('feedback/',views.feedback,name="feedback"),  
     path('bookingpage/<int:id>/',views.bookingpage,name="bookingpage"),
     path('bookdata/',views.bookdata,name="bookdata"),
     # path('bookingdata/',views.bookingdata,name="bookingdata"),
     path('',views.loginpage,name="loginpage"),
     path('logindata/',views.logindata,name="logindata"),
     path('user_login/',views.user_login,name="user_login"),
     path('user_logout/',views.user_logout,name="user_logout"),
     path('servicedetails/<int:id>/',views.servicedetails,name="servicedetails"),
     path('invoice_view/<int:booking_id>/',views.invoice_view,name="invoice_view"),


    
]
