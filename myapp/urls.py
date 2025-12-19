from django.urls import path
from .views import main, menu, login, register

urlpatterns = [
    path('', main, name='main'),
    path('menu/', menu, name='menu'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]
