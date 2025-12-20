from django.urls import path
from myapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.start_page, name='start'),  # головна перевірка
    path('main/', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),

]
