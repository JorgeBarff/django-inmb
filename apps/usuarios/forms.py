from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=15, required=False)
    nombres = forms.CharField(max_length=150, required=False)
    apellidos = forms.CharField(max_length=150, required=False)
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ("username", "email", "telefono", "nombres", "apellidos", "foto_perfil", "password1", "password2")
