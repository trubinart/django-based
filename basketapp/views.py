from django.shortcuts import render
from mainapp.models import Products
from basketapp.models import Basket
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404


def basket_add(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    baskets = Basket.objects.all().filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
