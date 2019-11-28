from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def add_to_wishlist(request):  
   template = loader.get_template('add_to_wishlist.html')
   return HttpResponse(template.render({"active_tab":"add_to_wishlist","request":request})) 