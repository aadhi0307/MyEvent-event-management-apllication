from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('admindata/',views.admindata,name='admindata'),
    path('adminsignin/',views.adminsignin,name='adminsignin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
]
