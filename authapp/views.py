from django.shortcuts import render

# Create your views here.

def login(request):
    content = {
        'title': 'GeekShop - Авторизация'
    }
    return render(request, 'authapp/login.html', content)

def register(request):
    content = {
        'title': 'GeekShop - Регистрация'
    }
    return render(request, 'authapp/register.html', content)