from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def shop(request):  
   template = loader.get_template('shop.html')
   return HttpResponse(template.render({"active_tab":"shop","request":request})) 