from django.urls import path
from myapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.start_page, name='start'),  # головна перевірка
    path('main/', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('breakfest/', views.breakfest, name='breakfest'),
    path('salat/', views.salat, name='salat'),
    path('sup/', views.sup, name='sup'),
    path('drink/', views.drink, name='drink'),
    path('desert/', views.desert, name='desert'),
    path('ohibka/', views.ohibka, name='ohibka'),
    path('sirniku/', views.sirniku, name='sirniku'),
    path('tostu/', views.tostu, name='tostu'),
    path('vafli/', views.vafli, name='vafli'),
    path('voda/', views.voda, name='voda'),
    path('tea/', views.tea, name='tea'),
    path('smyzi/', views.smyzi, name='smyzi'),
    path('kok/', views.kok, name='kok'),
    path('kava/', views.kava, name='kava'),


]   