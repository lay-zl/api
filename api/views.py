from django.shortcuts import render,redirect
from .models import Categories,Product
from .aform import CategorForm,ProductForm
from rest_framework.response import responses
from rest_framework import viewsets
from .seralizers import *
# Create your views here.

def index(req):
    if req.method == 'POST':
        data = CategorForm(req.POST,None)

        if data.is_valid():
            value = data.cleaned_data['new_catagory']

            a=Categories.objects.filter(new_catagory=value).first()
            if not a:
                data.save()
    form = CategorForm()
    c=Categories.objects.all()
    return render(req,'index.html',{'form':form,'c':c})

def add_product(req):
    if req.method == 'POST':
        data=ProductForm(req.POST,None)
        if data.is_valid():
            data.save()
            return redirect('/')
    form = ProductForm()
    return render(req,'add_product.html',{'form':form})

def show_product(req):
    ob= Product.objects.all()
    return render(req,'showproduct.html',{'ob':ob})

def edit_catgy(req,id):
    if req.method == 'POST':
        ob = Categories.objects.get(id=id)
        f = CategorForm(req.POST, instance=ob)
        f.save()
        return render(req,'edit.html',{'ob':'Data updated sucesfully..!!'})
    c=Categories.objects.get(id=id)
    ob= CategorForm(instance=c)
    return render(req,'edit.html',{'ob':ob})

def delete_catgy(req,id):
    c=Categories.objects.get(id=id)
    c.delete()
    return render(req,'delete.html',{'msg':'Record deleted Sucessfully..!!'})



class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSeralizer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer