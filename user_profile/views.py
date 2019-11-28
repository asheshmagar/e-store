from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def profile(request):  
   user = User.objects.get(username=request.user.username)
   template = loader.get_template('profile.html')
   return HttpResponse(template.render({
      "active_tab":"dashboard",
      "request":request,
      "user":user})) 