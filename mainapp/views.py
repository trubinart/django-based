from django.shortcuts import render
import json
import datetime
from mainapp.models import Category, Products

# Create your views here.
def index(request):
    dateTime = datetime.datetime.now()
    content = {
        'title': 'GeekShop Store',
        'h1': 'GeekShop Store',
        'date': dateTime
    }
    return render(request,'mainapp/index.html', content)

def products(request):
    content = {
        'title': 'GeekShop - Каталог',
        'h1': 'GeekShop',
        'products': Products.objects.all(),
    }
    return render(request,'mainapp/products.html', content)