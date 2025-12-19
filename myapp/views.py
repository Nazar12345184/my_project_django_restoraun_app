from django.shortcuts import render

def main(request):
    return render(request, 'main.html', {"main": main})

def menu(request):
    return render(request, 'menu.html')


def login(request): 
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# Create your views here.
