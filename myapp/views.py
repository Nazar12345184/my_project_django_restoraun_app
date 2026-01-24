from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import LoginForm, PostForm
from .models import com, menuu


# ---------------- БАЗОВІ ----------------

def start_page(request):
    if request.user.is_authenticated:
        return redirect('menu')
    return redirect('main')


def main(request):
    return render(request, 'main.html')


def menu(request):
    return render(request, 'menu.html')


def ohibka(request):
    return render(request, 'ohibka.html')








# ---------------- BREAKFEST ----------------

def breakfest(request):
    return render(request, 'breakfest/breakfest.html')


def sirniku(request):
    return render(request, 'breakfest/sirniku/sirniku.html')


def sirniku_mal(request):
    return render(request, 'breakfest/sirniku/mal.html')


def sirniku_shok(request):
    return render(request, 'breakfest/sirniku/shok.html')


def sirniku_sol(request):
    return render(request, 'breakfest/sirniku/sol.html')


def tostu(request):
    return render(request, 'breakfest/tostu/tostu.html')


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


def vafli(request):
    return render(request, 'breakfest/vafli/vafli.html')


def vafli_maldjm(request):
    return render(request, 'breakfest/vafli/maldjm.html')


def vafli_med(request):
    return render(request, 'breakfest/vafli/med.html')


def vafli_poldjm(request):
    return render(request, 'breakfest/vafli/poldjm.html')


def vafli_sirop(request):
    return render(request, 'breakfest/vafli/sirop.html')


# ---------------- SALAT ----------------

def salat(request):
    return render(request, 'salat/salat.html')


def ol(request):
    return render(request, 'salat/ol/ol.html')


def shezar(request):
    return render(request, 'salat/shezar/shezar.html')

def grech(request):
    return render(request, 'salat/grech/gresh.html')


def zavok(request):
    return render(request, 'salat/zavok/zavok.html')

def avokado(request):
    return render(request, 'salat/avokado/avokado.html')


# ---------------- SUP ----------------

def sup(request):
    return render(request, 'sup/sup.html')


def frik(request):
    return render(request, 'sup/frik/frik.html')


def bul(request):
    return render(request, 'sup/bul/bul.html')


def borch(request):
    return render(request, 'sup/borch/borch.html')

def zelborch(request):
    return render(request, 'sup/zelborch/zelborch.html')


# ---------------- DRINK ----------------

def drink(request):
    return render(request, 'drink/drink.html')


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

############################################

def espresso(request):
    comm = com.objects.filter(name__name='espresso')
    return render(request, 'drink/kava/espresso.html', context={'comm': comm})

def espressocom(request):
    item = get_object_or_404(menuu, name='espresso')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("espresso")
    else:
        form = PostForm()

    return render(request, 'drink/kava/espressocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='espresso')
    return render(request, 'drink/kava/espresso.html', context={'comm': comm})

#######################################
def americano(request):
    comm = com.objects.filter(name__name='americano')
    return render(request, 'drink/kava/americano.html', context={'comm': comm})


def americanocom(request):
    item = get_object_or_404(menuu, name='americano')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("americano")
    else:
        form = PostForm()

    return render(request, 'drink/kava/americanocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/americano.html', context={'comm': comm})

######################################
    


def kapuchino(request):
    comm = com.objects.filter(name__name='kapuchino')
    return render(request, 'drink/kava/kapuchino.html', context={'comm': comm})

def kapuchinocom(request):
    item = get_object_or_404(menuu, name='kapuchino')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kapuchino")
    else:
        form = PostForm()

    return render(request, 'drink/kava/kapuchinocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/kapuchino.html', context={'comm': comm})

###############################################

def latte(request):
    comm = com.objects.filter(name__name='latte')
    return render(request, 'drink/kava/latte.html', context={'comm': comm})

def lattecom(request):
    item = get_object_or_404(menuu, name='latte')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("latte")
    else:
        form = PostForm()

    return render(request, 'drink/kava/lattecom.html', {"form": form, "item": item})



def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/latte.html', context={'comm': comm})

###################################

def kakao(request):
    comm = com.objects.filter(name__name='kakao')
    return render(request, 'drink/kava/kakao.html', context={'comm': comm})

def kakaocom(request):
    item = get_object_or_404(menuu, name='kakao')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kakao")
    else:
        form = PostForm()

    return render(request, 'drink/kava/kakaocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/kakao.html', context={'comm': comm})

##################################

def mol(request):
    comm = com.objects.filter(name__name='mol')
    return render(request, 'drink/kok/mol.html', context={'comm': comm})

def molcom(request):
    item = get_object_or_404(menuu, name='mol')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("mol")
    else:
        form = PostForm()

    return render(request, 'drink/kok/molcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/mol.html', context={'comm': comm})

##################################

def blla(request):
    comm = com.objects.filter(name__name='blla')
    return render(request, 'drink/kok/blla.html', context={'comm': comm})

def bllacom(request):
    item = get_object_or_404(menuu, name='blla')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("blla")
    else:
        form = PostForm()

    return render(request, 'drink/kok/bllacom.html', {"form": form, "item": item})


def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/blla.html', context={'comm': comm})

############################

def mohito(request):
    comm = com.objects.filter(name__name='mohito')
    return render(request, 'drink/kok/mohito.html', context={'comm': comm})

def mohitocom(request):
    item = get_object_or_404(menuu, name='mohito')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("mohito")
    else:
        form = PostForm()

    return render(request, 'drink/kok/mohitocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/mohito.html', context={'comm': comm})

############################


def cherry(request):
    comm = com.objects.filter(name__name='cherry')
    return render(request, 'drink/smyzi/cherry.html', context={'comm': comm})

def cherrycom(request):
    item = get_object_or_404(menuu, name='cherry')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("cherry")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/cherrycom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/cherry.html', context={'comm': comm})

##############################

def polynisa(request):
    comm = com.objects.filter(name__name='polynisa')
    return render(request, 'drink/smyzi/polynisa.html', context={'comm': comm})

def polynisacom(request):
    item = get_object_or_404(menuu, name='polynisa')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("polynisa")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/polynisacom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/polynisa.html', context={'comm': comm})

#####################

def banan(request):
    comm = com.objects.filter(name__name='banan')
    return render(request, 'drink/smyzi/banan.html', context={'comm': comm})

def banancom(request):
    item = get_object_or_404(menuu, name='banan')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("banan")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/banancom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/banan.html', context={'comm': comm})

#############################################

def green(request):
    comm = com.objects.filter(name__name='green')
    return render(request, 'drink/tea/green.html', context={'comm': comm})

def greencom(request):
    item = get_object_or_404(menuu, name='green')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("green")
    else:
        form = PostForm()

    return render(request, 'drink/tea/greencom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/green.html', context={'comm': comm})

#########################

def black(request):
    comm = com.objects.filter(name__name='black')
    return render(request, 'drink/tea/black.html', context={'comm': comm})

def blackcom(request):
    item = get_object_or_404(menuu, name='black')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("black")
    else:
        form = PostForm()

    return render(request, 'drink/tea/blackcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/black.html', context={'comm': comm})

###############################

def night(request):
    comm = com.objects.filter(name__name='night')
    return render(request, 'drink/tea/night.html', context={'comm': comm})

def nightcom(request):
    item = get_object_or_404(menuu, name='night')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("night")
    else:
        form = PostForm()

    return render(request, 'drink/tea/nightcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/night.html', context={'comm': comm})

##########################

def sik(request):
    comm = com.objects.filter(name__name='sik')
    return render(request, 'drink/voda/sik.html', context={'comm': comm})

def sikcom(request):
    item = get_object_or_404(menuu, name='sik')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sik")
    else:
        form = PostForm()

    return render(request, 'drink/voda/sikcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/sik.html', context={'comm': comm})   

##########################

def sprite(request):
    comm = com.objects.filter(name__name='sprite')
    return render(request, 'drink/voda/sprite.html', context={'comm': comm})    

def spritecom(request):
    item = get_object_or_404(menuu, name='sprite')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sprite")
    else:
        form = PostForm()

    return render(request, 'drink/voda/spritecom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/sprite.html', context={'comm': comm})
##################################

def kola(request):
    comm = com.objects.filter(name__name='kola')
    return render(request, 'drink/voda/kola.html', context={'comm': comm})

def kolacom(request):
    item = get_object_or_404(menuu, name='kola')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kola")
    else:
        form = PostForm()

    return render(request, 'drink/voda/kolacom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/kola.html', context={'comm': comm})
#################################


def yzvar(request):
    comm = com.objects.filter(name__name='yzvar')
    return render(request, 'drink/voda/yzvar.html', context={'comm': comm})

def yzvarcom(request):
    item = get_object_or_404(menuu, name='yzvar')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("yzvar")
    else:
        form = PostForm()

    return render(request, 'drink/voda/yzvarcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/yzvar.html', context={'comm': comm})

##########################


def krevetka(request):
    return render(request, 'drink/krevetka.html')


# ---------------- DESERT ----------------

def desert(request):
    return render(request, 'desert/desert.html')

###############################
def moroz(request):
    comm = com.objects.filter(name__name='moroz')
    return render(request, 'desert/moroz/moroz.html', context={'comm': comm})

def morozcom(request):
    item = get_object_or_404(menuu, name='moroz')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("moroz")
    else:
        form = PostForm()

    return render(request, 'desert/moroz/morozcom.html', {"form": form, "item": item})


def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/moroz/moroz.html', context={'comm': comm})

#################################


def nap(request):
    comm = com.objects.filter(name__name='nap')
    return render(request, 'desert/nap/nap.html', context={'comm': comm})

def napcom(request):
    item = get_object_or_404(menuu, name='nap')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("nap")
    else:
        form = PostForm()

    return render(request, 'desert/nap/napcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/nap/nap.html', context={'comm': comm})

##################################

def tir(request):
    comm = com.objects.filter(name__name='tir')
    return render(request, 'desert/tir/tir.html', context={'comm': comm})

def tircom(request):
    item = get_object_or_404(menuu, name='tir')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("tir")
    else:
        form = PostForm()

    return render(request, 'desert/tir/tircom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/tir/tir.html', context={'comm': comm})

# ---------------- AUTH ----------------

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, 'Невірний логін або пароль')
        return self.form_invalid(form)


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

