from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from checkout.forms import CheckoutForm

# Create your views here.
def checkout(request):
   csrfContext = RequestContext(request)
   checkout_form = CheckoutForm()
   return render(request,'checkout.html',
      {
         'form': checkout_form,
         "active_tab":"checkout",
         "request":request
      },
      csrfContext) 