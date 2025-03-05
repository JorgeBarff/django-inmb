

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib import messages  # Importa messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail



def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            generar_password = form.cleaned_data.get("generar_password")

            if generar_password:
                contrasena = form.cleaned_data["password1"]
                user.set_password(contrasena)  # Guarda la contraseña encriptada
                send_mail(
                    'Tu cuenta ha sido creada',
                    f'Tu usuario es {user.username} y tu contraseña es: {contrasena}',
                    'noreply@crm.com',  # Cambia esto por tu email
                    [user.email],
                    fail_silently=False,
                )

            user.save()
            messages.success(request, 'Cuenta creada exitosamente. Revisa tu correo para obtener la contraseña.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            generar_password = form.cleaned_data.get("generar_password")

            if generar_password:
                contrasena = form.cleaned_data["password1"]
                user.set_password(contrasena)  # Guarda la contraseña encriptada
                send_mail(
                    'Tu cuenta ha sido creada',
                    f'Tu usuario es {user.username} y tu contraseña es: {contrasena}',
                    'noreply@crm.com',  # Cambia esto por tu email
                    [user.email],
                    fail_silently=False,
                )

            user.save()
            messages.success(request, 'Cuenta creada exitosamente. Revisa tu correo para obtener la contraseña.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}. Has iniciado sesión correctamente.')
                return redirect('dashboard')
        messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})
