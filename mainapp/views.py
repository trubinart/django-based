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

def products(request, category_id=None):
    content = {
        'title': 'GeekShop - Каталог',
        'h1': 'GeekShop',
        'products': Products.objects.filter(category_id=category_id) if category_id else Products.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request,'mainapp/products.html', content)