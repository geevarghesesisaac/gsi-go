from django.urls import path,include
from django.urls import path, re_path
from home.views import *
from dealer import *
from customer import *
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
]
