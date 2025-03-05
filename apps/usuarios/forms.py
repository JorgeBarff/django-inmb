import random
import string
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

def generar_contrasena():
    """Genera una contraseña aleatoria segura."""
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(12))  # 12 caracteres aleatorios

class RegistroForm(UserCreationForm):
    generar_password = forms.BooleanField(
        required=False, 
        label="Generar contraseña automáticamente",
        widget=forms.CheckboxInput()
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(), 
        required=False  # Hacemos que sea opcional
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), 
        required=False  # Hacemos que sea opcional
    )

    class Meta:
        model = Usuario
        fields = ["username", "email", "telefono", "nombres", "apellidos", "foto_perfil", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        generar_password = cleaned_data.get("generar_password")

        if generar_password:
            contrasena_auto = generar_contrasena()
            cleaned_data["password1"] = contrasena_auto
            cleaned_data["password2"] = contrasena_auto
            self.instance.set_password(contrasena_auto)  # Guarda la contraseña encriptada
        else:
            if not cleaned_data.get("password1") or not cleaned_data.get("password2"):
                raise forms.ValidationError("Debes ingresar una contraseña o seleccionar la opción de generación automática.")
        
        return cleaned_data
