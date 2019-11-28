from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def order_complete(request):  
   template = loader.get_template('order_complete.html')
   return HttpResponse(template.render({"active_tab":"order_complete","request":request})) 