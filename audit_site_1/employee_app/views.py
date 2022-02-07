from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def index(request):
    print(request)
    return HttpResponse('Fu**ing first employee_app responce. Or not?')


def index_employees(request):
    employees = Employee.objects.all()
    res = '<h1>Список сотрудников</h1>'
    for item in employees:
        res += f'<div>\n<p>{item.first_name}</p>\n' \
               f'<p>{item.last_name}</p>\n' \
               f'<p>{item.position}</p>\n' \
               f'<p>{item.created_at}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Тестовая страница Employee_app</h1>')


def test2(request):
    return HttpResponse('<h1>Тестовая страница Employee_app. || Second edition ||</h1>')
