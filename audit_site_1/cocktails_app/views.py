
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cocktail


# Create your views here.

def index_cocktails(request):
    cocktails = Cocktail.objects.all()
    res = '<h1>Список коктейлей</h1>'
    for item in cocktails:
        res += f'<div>\n<p>{item.name}</p>\n<p>{item.bar_price}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def test_cocktails(request):
    return HttpResponse('<h1>Тестовая страница для коктейлей. ?</h1>')
