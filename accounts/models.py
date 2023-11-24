from django.db import models

# Create your models here.


class admindb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.IntegerField()
    image=models.ImageField(upload_to="account",null=True,blank=True)
    pwd=models.CharField(max_length=50)
    cpwd=models.CharField(max_length=50)