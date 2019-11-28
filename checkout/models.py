#this file is not used.
from django.db import models

class Checkout(models.Model):
    country = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    first_address = models.CharField(max_length=30)
    second_address = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    email_address = models.EmailField()
    phone_number = models.IntegerField()
    payment_option = models.CharField(max_length=30)
    terms_agreed = models.BooleanField()
