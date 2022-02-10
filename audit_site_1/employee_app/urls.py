from django.urls import path
from .views import *

# Employee_app
urlpatterns = [
    path('', index_employees),
    path('test/', test),
    path('test2/', test2),
]
