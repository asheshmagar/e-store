

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from login.forms import LoginForm, SignupForm
from django.contrib.auth import login as auth_login, authenticate
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers
from rest_framework.response import Response
import requests
import datetime
from django.contrib.auth import logout

# @csrf_protect
# def login(request):  
#     if request.method == 'POST': 
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('/show')
#     csrfContext = RequestContext(request)
#     login_form = LoginForm()
#     return render(request,'login.html',{'form': login_form},csrfContext)

@csrf_protect
def signup(request):
    if request.user.is_authenticated:
        return redirect('/'); 
    if request.method == 'POST': 
        signup = SignupForm(request.POST)
        if signup.is_valid():
            response = requests.post('http://localhost:8000/api/v1/register/', request.POST)
            print('response', response.text)
            if response.status_code == 200:
                username = signup.cleaned_data.get('username')
                raw_password = signup.cleaned_data.get('password')
                print(username)
                print(raw_password)
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                   auth_login(request, user)
                   return redirect('/')
                else:
                    return HttpResponse("Problem while registering.")
            
    
    csrfContext = RequestContext(request)
    signup_form = SignupForm()
    return render(request,'register.html',{'form': signup_form,"active_tab":"login"},csrfContext)

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    def create(self, request):
        print("new request")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
           password = request.data.get("password")
           user = serializer.save()
           user.set_password(password)
           user.save()
        
           return Response(status=200,data={"msg": "User has been registered."})
        else:
           return Response(status=500,data={"msg": "Unable to register user."})

    def list(self, request):
        return Response(status=403,data={"msg": "API not allowed."})
    
    def retrieve(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."}) 

class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer

    def create(self, request):
        print("new request")
        try:
            # print(request.COOKIES)
            last_login = request.COOKIES.get('last_login_date',{})
            print("last login date in cookie", last_login)
            username = request.data.get('username')
            loggedin_status = request.session.get('loggedin_status', {})
            loggedIn = loggedin_status.get('loggedIn', False)
            if loggedIn:
                return Response(status=404,data={"success": False, "msg":"You've already loggedin."})
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session['loggedin_status'] = {
                    'loggedIn' : True,
                    'last_login_date': str(datetime.datetime.now())
                }
                #cookie example
                response = Response(status=200,data={"success": True})
                response.set_cookie('last_login_date', datetime.datetime.now())
                return response
            else:
                return Response(status=404,data={"success": False})
        except Exception as e:
            print(e)
            return Response(status=501,data={"msg": "Problem while logging in user."})

    def list(self, request):
        return Response(status=403,data={"msg": "API not allowed."})

    def retrieve(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})    

class LogoutViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.LogoutSerializer

    def create(self, request):
        print("new request")
        try:

            # username = request.data.get('username')
            loggedin_status = request.session.get('loggedin_status', {})
            loggedIn = loggedin_status.get('loggedIn', False)
            if loggedIn:
                logout(request)
                return Response(status=200,data={"success": True, "msg":"You've successfully logged out."})
            else:
                return Response(status=404,data={"success": False, "msg":"You've already logged out."})
            # logout(request)
            # return Response(status=200,data={"success": True, "msg":"You've successfully logged out."})
        except Exception as e:
            print(e)
            return Response(status=501,data={"msg": "Problem while logging out user."})

    def list(self, request):
        return Response(status=403,data={"msg": "API not allowed."})

    def retrieve(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})    
