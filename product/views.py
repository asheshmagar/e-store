from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product, Color, Size
from django.http import JsonResponse
from product.forms import ProductForm
import json
from rest_framework.parsers import FileUploadParser
from rest_framework import response
from rest_framework.decorators import action
from rest_framework import parsers

from rest_framework import viewsets
from . import serializers
from rest_framework.response import Response

# Create your views here.
def show(request):
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products}) 

def product(request):  
    if request.method == "POST":   
        print("inside post")
        print(request.POST)
        sizes = request.POST.getlist("psize")
        all_sizes = []
        for size in sizes:
            print("checking for size", size)
            s = Size.objects.filter(size=size)
            for a in s:
                print("sizes", a)
                all_sizes.append(a.id)
        postdata = request.POST.copy()
        postdata["psize"] = all_sizes
        print("all sizes", postdata["psize"])
        colors = request.POST.getlist("pcolor")
        all_colors = []
        for color in colors:
            print("checking fro color", color)
            s = Color.objects.filter(color=color)
            for a in s:
                print("colors", a)
                all_colors.append(a.id)
        postdata = request.POST.copy()
        postdata["pcolor"] = all_colors

        form = ProductForm(postdata, request.FILES) 
        if form.is_valid():  
            try:
                print("saving form")  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'add_product.html',{'form':form})

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})

def raw_sql(request):
    name = ""
    for p in Product.objects.raw('SELECT * FROM products'):
        name = name + " " + p.pname
    return JsonResponse({'result':name})

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(
        detail=True,
        methods=['PUT'],
        serializer_class=serializers.ProductImageSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)