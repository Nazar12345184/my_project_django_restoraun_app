from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView
from .forms import LoginForm
from .models import menuu

#                        XZ
def main(request):
    return render(request, 'main.html')


def menu(request):
    return render(request, 'menu.html')


def register(request):
    return render(request, 'register.html')


def start_page(request):
    if request.user.is_authenticated:
        return redirect('menu')
    else:
        return redirect('main')  


#           LOGIN
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('menu')  

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)


#                REGISTER

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # після реєстрації → логін


#                 HOME

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'main.html'
    model = menuu
    context_object_name = 'all_items'
    # model = Item  # розкоментуйте після створення моделі