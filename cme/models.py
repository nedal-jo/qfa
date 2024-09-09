from django.db import models

# Create your models here.

class SipPhone(models.Model):
    pool = models.IntegerField()
    mac =  models.CharField(max_length=90)
    type = models.IntegerField()
    username= models.CharField(max_length=90)
    password = models.CharField(max_length=90)
    number1 = 
    number2 =
    extras = models.CharField(max_length=90)
class CmePhone(models.Model):
    ephone = models.IntegerField()
    mac = models.CharField(max_length=90)
    type = models.IntegerField()
    button = models.IntegerField()
    extras = models.CharField(max_length=90)
class SipBook(models.Model):
    dn = models.IntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length=90)
    label = models.CharField(max_length=90)
    extras = models.CharField(max_length=90)
class CmeBook(models.Model):
    dn = models.IntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length=90)
    label = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    extras = models.CharField(max_length=90)
