from django.urls import path,include
from dealer.views import *
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth_view, name='auth_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('manage_vehicles/', views.manage_vehicles, name='manage_vehicles'),
    path('order_list/', views.order_list, name='order_list'),
    path('complete/', views.complete, name='complete'),
    path('history/', views.history, name='history'),
    path('delete/', views.delete, name='delete'),
]
