from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/login')
def about(request):  
   template = loader.get_template('about.html')
   return HttpResponse(template.render({"active_tab":"about","request":request})) 