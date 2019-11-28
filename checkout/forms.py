from django import forms  
from . import models
from django.conf import settings
import os
import json

file=os.path.join( settings.BASE_DIR, 'checkout/static/data/countries.json' )

def getCountries():
    with open(file) as f:
        y = json.load(f)

    a = []
    for key,value in y.items():
        a.append((key,value))
    return a

countries = getCountries()
payment_options = [(1,'Cash on Delivery'), (2,'Paypal'), (3,'Direct Bank Transfer'), (4,'esewa')]

class CheckoutForm(forms.ModelForm):
    country = forms.CharField(
        max_length=30,
        widget=forms.Select(choices = countries, attrs={'class': "form-control"}),
    )
    payment_option = forms.ChoiceField(
        choices = payment_options,
        widget=forms.RadioSelect(attrs={'class': "payment-options"})
    )
    terms_agreed = forms.BooleanField(required=True)
    first_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your firstname"
            }))
    last_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your lastname"
            }))
    company_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Company Name"
            }))
    first_address = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your firstaddress"
            }))
    second_address = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Second Address"
            }))

    town = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Town or City"
            }))

    state = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "State Province"
            }))
    zip_code = forms.IntegerField(
        widget=forms.NumberInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Zip / Postal"
            }))
    email_address = forms.EmailField(
        widget=forms.EmailInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Email Address"
            }))

    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Phone Number"
            }))

    class Meta:  
        model = models.Checkout
        fields = "__all__"