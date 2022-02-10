from django.urls import path
from .views import *

#######
urlpatterns = [
    path('', index_cocktails),
    path('test/', test_cocktails),
]