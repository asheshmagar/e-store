from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from product.models import Product

# Create your views here.
def home(request): 
   products = Product.objects.all() 
   print("products", products)
   template = loader.get_template('index.html')
   return HttpResponse(template.render({"active_tab":"home","request":request,'products':products})) 