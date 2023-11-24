from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class categorydb(models.Model):
#     category=models.CharField(max_length=50,null=True,blank=True)
#     cimage=models.ImageField(upload_to="category",null=True,blank=True)
#     description=models.CharField(max_length=200,null=True,blank=True)

# class venuedb(models.Model):
#     VenueName=models.CharField(max_length=50,null=True,blank=True)
#     venueAddress =models.CharField(max_length=100,null=True,blank=True)
#     venueRent=models.IntegerField(null=True,blank=True)
#     venueDescription=models.CharField(max_length=500,null=True,blank=True)
#     venueImage=models.ImageField(upload_to="Venues",null=True,blank=True)

# class cateringdb(models.Model):
#     catname=models.CharField(max_length=50,null=True,blank=True)
#     catAddress =models.CharField(max_length=100,null=True,blank=True)
#     catrent=models.IntegerField(null=True,blank=True)
#     catDescription=models.CharField(max_length=500,null=True,blank=True)
#     catImage=models.ImageField(upload_to="catering",null=True,blank=True)

# class mediadb(models.Model):
#     medianame=models.CharField(max_length=50,null=True,blank=True)
#     mediaAddress =models.CharField(max_length=100,null=True,blank=True)
#     mediarent=models.IntegerField(null=True,blank=True)
#     mediaDescription=models.CharField(max_length=500,null=True,blank=True)
#     mediapic=models.ImageField(upload_to="photography",null=True,blank=True)

# class transportationdb(models.Model):
#     transname=models.CharField(max_length=50,null=True,blank=True)
#     transAddress=models.CharField(max_length=100,null=True,blank=True)
#     transrent=models.IntegerField(null=True,blank=True)
#     transDescription=models.CharField(max_length=500,null=True,blank=True)
#     transImage=models.ImageField(upload_to="transportation",null=True,blank=True)


class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    logo=models.ImageField(upload_to="category_logo")
    def __str__(self):
        return self.name

class Service(models.Model):
    s_name = models.CharField(max_length=50,null=True,blank=True)
    service_name = models.CharField(max_length=50,null=True,blank=True)
    service_address = models.CharField(max_length=100,null=True,blank=True)
    service_rent = models.IntegerField(null=True,blank=True)
    service_description = models.CharField(max_length=500,null=True,blank=True)
    service_image = models.ImageField(upload_to="service",null=True,blank=True)

class admindata(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    pwd=models.CharField(max_length=50, null=True, blank=True)
    cpwd=models.CharField(max_length=50, null=True, blank=True)




