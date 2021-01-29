from django.shortcuts import render
import json
import datetime
from .models import Category, Products

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
    with open('./mainapp/fixtures/products.json') as poducts:
        data = json.load(poducts)

    content = {
        'title': 'GeekShop - Каталог',
        'h1': 'GeekShop',
        'products': Products.objects.all(),
    }
    return render(request,'mainapp/products.html', content)
