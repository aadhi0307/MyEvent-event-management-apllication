from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    pwd=models.CharField(max_length=50, null=True, blank=True)

class Contactdata(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

class Feedback(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    select_service=models.CharField(max_length=50, null=True, blank=True)
    feedbacks = models.TextField(max_length=100, null=True, blank=True)

class booking(models.Model):
    book_name=models.CharField(max_length=50, null=True, blank=True)
    book_email=models.CharField(max_length=50, null=True, blank=True)
    book_date=models.DateField()
    book_rent=models.IntegerField(null=True, blank=True)
    book_service=models.CharField(max_length=50,null=True, blank=True)
    book_message=models.CharField(max_length=50, null=True, blank=True)
   