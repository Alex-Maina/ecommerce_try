from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def store (request):
    products= Product.objects.all()
    
    context ={'products':products}
    return render(request, 'store.html', context)

def checkout (request):
    
    context ={}
    return render(request, 'checkout.html', context)

def buy (request):
    
    context ={}
    return render(request, 'checkout_form.html', context)