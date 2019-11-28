from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def blog(request):  
   template = loader.get_template('blog.html')
   return HttpResponse(template.render({"active_tab":"blog","request":request})) 