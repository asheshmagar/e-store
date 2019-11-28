from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from product.models import Product,Color

# Create your views here.
def new_product_detail(request, id):
   print("id", id) 
   product = Product.objects.get(id=id)
   colors = []
   for color in product.pcolor.all():
      colors.append(color.color)
   print(product.pimage)
   template = loader.get_template('product_detail.html')
   return HttpResponse(template.render({"colors":colors,"product":product,"active_tab":"product_detail","request":request})) 

def product_detail(request):
   template = loader.get_template('product_detail.html')
   return HttpResponse(template.render({"active_tab":"product_detail","request":request})) 