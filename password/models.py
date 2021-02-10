from django.db import models

from django.urls import reverse

# from django import forms

# Create your models here.
class User(models.Model):
    # # Usually Django gives each model an ID with AutoField if no primary. Thus, normally this field is not needed.
    # # https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fields
    # id = models.AutoField(primary_key=True)
    lastName    = models.CharField(max_length=60)
    firstName   = models.CharField(max_length=50)
    password    = models.CharField(max_length=100, help_text='Input password here (max length = 100).')
    email       = models.EmailField(help_text='Input email address here (max length = 254).')
    auth        = models.ForeignKey('AuthLevel', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['lastName', 'firstName']

    def get_absolute_url(self):
        return reverse('user-list')#, args=[str(self.id)])

    def __str__(self):
        return self.lastName + self.firstName

class AuthLevel(models.Model):
    auth        = models.CharField(max_length=100, help_text='Input Auth Level here. e.g: Admin, Peer, Acquaintance (max length = 50).')

    def get_absolute_url(self):
        return reverse('auth-level-list')#, args=[str(self.id)])

    # To display auth instead of showing 'AuthLevel Object (1)'
    def __str__(self):
        return self.auth

class Account(models.Model):
    accountName     = models.CharField(max_length=100, help_text='Input the name of the account (max length = 100).')
    summary         = models.CharField(max_length=300, help_text='Input summary of the account here (max length = 300).', null=True, blank=True)
    userID          = models.CharField(max_length=80, help_text='Input the user id of the account (max length = 80).', null=True, blank=True)
    password        = models.CharField(max_length=300, help_text='Input password of the account here (max length = 300).', null=True, blank=True)
    email           = models.EmailField(help_text='Input email address of the account here (max length = 254).', null=True, blank=True)
    auth            = models.ForeignKey('AuthLevel', on_delete=models.RESTRICT)

    # I use Snake case here instead of Camel case naming to avoid typo-error become difficult to discover.
    date_of_created = models.DateField(null=True, blank=True)
    date_of_deleted = models.DateField(null=True, blank=True)

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('account-list')#, args=[str(self.id)])

    def __str__(self):
        return self.accountName




















