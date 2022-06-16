from cgi import test
#from tkinter import CASCADE
from django.db import models
from django.forms import DateField, DateTimeField
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    wallet=models.CharField(max_length=255,unique=True ,null=False,blank=False)
    first_name=models.CharField(max_length=255,null=True, blank=True)
    last_name=models.CharField(max_length=255,null=True, blank=True)
    email=models.EmailField(max_length = 255,null=True, blank=True)
    phone=models.CharField(max_length=255,null=True, blank=True)
    avatar=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.wallet

class Domain(models.Model):
    id_contract = models.PositiveIntegerField()
    profile = models.CharField(max_length= 255)
    domain = models.CharField(max_length= 255, unique=True)
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain
        #return "Nombre: %s, ID_dominio:%s"%(self.domain,self.id)

class DomainCredentials(models.Model):
    id_contract = models.PositiveIntegerField()
    domain= models.CharField(max_length= 255, unique=True, primary_key=True)
    seedPhrase = models.CharField(max_length= 255)
    secretKey = models.CharField(max_length= 255)
    publicKey = models.CharField(max_length= 255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain 
        #return "Dominio: %s, ID_credential:%s"%(self.domain.domain,self.domain.id)

