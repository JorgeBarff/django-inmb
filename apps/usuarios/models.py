# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)  # Hacemos el email único y obligatorio
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nombres = models.CharField(max_length=150, blank=True, null=True)
    apellidos = models.CharField(max_length=150, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
