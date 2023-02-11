from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=25, blank=False)
    lname = models.CharField(max_length=25, blank=False)
    email = models.EmailField(max_length=120, unique=True, blank=False)
    password = models.CharField(max_length=56, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    country_code = models.CharField(max_length=3, blank=False) 