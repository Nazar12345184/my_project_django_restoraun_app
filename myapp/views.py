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

def breakfest(request):
    return render(request, 'breakfest/breakfest.html')

def salat(request):
    return render(request, 'salat/salat.html')

def sup(request):
    return render(request, 'sup/sup.html')

def drink(request):
    return render(request, 'drink/drink.html')

def desert(request):
    return render(request, 'desert/desert.html')

def ohibka(request):
    return render(request, 'ohibka.html')

def sirniku(request):
    return render(request, 'breakfest/sirniku/sirniku.html')

def tostu(request):
    return render(request, 'breakfest/tostu/tostu.html')

def vafli(request):
    return render(request, 'breakfest/vafli/vafli.html')

def voda(request):
    return render(request, 'drink/voda/voda.html')

def tea(request):
    return render(request, 'drink/tea/tea.html')

def smyzi(request):
    return render(request, 'drink/smyzi/smyzi.html')

def kok(request):
    return render(request, 'drink/kok/kok.html')

def kava(request):
    return render(request, 'drink/kava/kava.html')

def espresso(request):
    return render(request, 'drink/kava/espresso.html')

def americano(request):
    return render(request, 'drink/kava/americano.html')

def kapuchino(request):
    return render(request, 'drink/kava/kapuchino.html')

def latte(request):
    return render(request, 'drink/kava/latte.html')

def kakao(request):
    return render(request, 'drink/kava/kakao.html')

def mol(request):
    return render(request, 'drink/kok/mol.html')

def blla(request):
    return render(request, 'drink/kok/blla.html')

def mohito(request):
    return render(request, 'drink/kok/mohito.html')

def cherry(request):
    return render(request, 'drink/smyzi/cherry.html')

def polynisa(request):
    return render(request, 'drink/smyzi/polynisa.html')

def banan(request):
    return render(request, 'drink/smyzi/banan.html')

def green(request):
    return render(request, 'drink/tea/green.html')

def black(request):
    return render(request, 'drink/tea/black.html')

def night(request):
    return render(request, 'drink/tea/1001night.html')

def sik(request):
    return render(request, 'drink/voda/sik.html')

def sprite(request):
    return render(request, 'drink/voda/sprite.html')

def kola(request):
    return render(request, 'drink/voda/kola.html')

def yzvar(request):
    return render(request, 'drink/voda/yzvar.html')

def grech(request):
    return render(request, 'salat/grech/gresh.html')

def krevetka(request):
    return render(request, 'salat/krevetka/krevetka.html')

# --- breakfest  ---
def sirniku_mal(request):
    return render(request, 'breakfest/sirniku/mal.html')

def sirniku_shok(request):
    return render(request, 'breakfest/sirniku/shok.html')

def sirniku_sol(request):
    return render(request, 'breakfest/sirniku/sol.html')

# ---     tostu      ---
def tostu_avo(request):
    return render(request, 'breakfest/tostu/avo.html')

def tostu_chdj(request):
    return render(request, 'breakfest/tostu/chdj.html')

def tostu_maldj(request):
    return render(request, 'breakfest/tostu/maldj.html')

def tostu_poldj(request):
    return render(request, 'breakfest/tostu/poldj.html')

def tostu_sur(request):
    return render(request, 'breakfest/tostu/sur.html')

# --- vafli  ---
def vafli_maldjm(request):
    return render(request, 'breakfest/vafli/maldjm.html')

def vafli_med(request):
    return render(request, 'breakfest/vafli/med.html')

def vafli_poldjm(request):
    return render(request, 'breakfest/vafli/poldjm.html')

def vafli_sirop(request):
    return render(request, 'breakfest/vafli/sirop.html')

# ---    salat    ---
def ol(request):
    return render(request, 'salat/ol/ol.html')

def shezar(request):
    return render(request, 'salat/shezar/shezar.html')

def zavok(request):
    return render(request, 'salat/zavok/zavok.html')


# ---  start page ----

def start_page(request):
    if request.user.is_authenticated:
        return redirect('menu')
    else:
        return redirect('main')  

# --- desert  ---
def moroz(request):
    return render(request, 'desert/moroz/moroz.html')

def nap(request):
    return render(request, 'desert/nap/nap.html')

def tir(request):
    return render(request, 'desert/tir/tir.html')

# --- sup  ---
def frik(request):
    return render(request, 'sup/frik/frik.html')

def bul(request):
    return render(request, 'sup/bul/bul.html')

def borch(request):
    return render(request, 'sup/borch/borch.html')

def zelborch(request):
    return render(request, 'sup/zelborch/zelborch.html')

# --- salat  ---
def avokado(request):
    return render(request, 'salat/avokado/avokado.html')


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
    success_url = reverse_lazy('login')  # після реєстрації — логін


#                 HOME

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'main.html'
    model = menuu
    context_object_name = 'all_items'
    
