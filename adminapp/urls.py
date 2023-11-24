from django.urls import path
from adminapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('service_add/',views.service_add,name="service_add"),
    path('service_data/',views.service_data,name="service_data"),
    path('service_display/',views.service_display,name="service_display"),
    path('service_edit/<int:dataid>',views.service_edit,name="service_edit"),
    path('service_update/<int:dataid>',views.service_update,name="service_update"),
    path('service_delete/<int:dataid>',views.service_delete,name="service_delete"),

    path('category_add/',views.category_add,name="category_add"),
    path('category_data/',views.category_data,name="category_data"),
    path('category_display/',views.category_display,name="category_display"),
    path('category_edit/<int:dataid>',views.category_edit,name="category_edit"),
    path('category_update/<int:dataid>',views.category_update,name="category_update"),
    path('category_delete/<int:dataid>',views.category_delete,name="category_delete"),

    path('admin_signin/',views.admin_signin,name="admin_signin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_data/',views.admin_data,name="admin_data"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('contact_display/',views.contact_display,name="contact_display"),
    path('bookings/',views.bookings,name="bookings"),
    path('booking_delete/<int:dataid>/',views.booking_delete,name="booking_delete"),
   
]
