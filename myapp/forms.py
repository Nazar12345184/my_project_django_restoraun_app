from django import forms
from django.contrib.auth.models import User
from .models import menuu, com


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = com
        fields = ["description"]