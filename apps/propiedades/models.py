# Create your models here.
# apps/propiedades/models.py
import os
from PIL import Image
from django.db import models

class ImagenPropiedad(models.Model):
# class Propiedad(models.Model):
    propiedad = models.ForeignKey('propiedades.ImagenPropiedad', on_delete=models.CASCADE, related_name='imagenes')
    # propiedad = models.ForeignKey('propiedades.propiedad', on_delete=models.CASCADE, related_name='imagenes')

    imagen = models.ImageField(upload_to='propiedades/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda la imagen original temporalmente

        if self.imagen:
            ruta_imagen = self.imagen.path
            # Abrir la imagen usando Pillow
            img = Image.open(ruta_imagen)
            img = img.convert("RGB")  # En caso de ser PNG con transparencia, convierne a RGB
            nueva_ruta = os.path.splitext(ruta_imagen)[0] + ".webp"
            # Guarda la imagen en formato WebP, con calidad optimizada (ejemplo: calidad 80)
            img.save(nueva_ruta, "WEBP", quality=80)
            # Elimina la imagen original y actualiza el campo de la imagen
            os.remove(ruta_imagen)
            self.imagen.name = self.imagen.name.rsplit('.', 1)[0] + ".webp"
            super().save(update_fields=['imagen'])


# apps/propiedades/models.py

# class Propiedad(models.Model):
#     TIPO_CHOICES = (
#         ('casa', 'Casa'),
#         ('departamento', 'Departamento'),
#         ('terreno', 'Terreno'),
#         # Agrega más tipos según tus necesidades
#     )
    
#     # Información básica
#     titulo = models.CharField(max_length=200)
#     descripcion = models.TextField()
#     precio = models.DecimalField(max_digits=12, decimal_places=2)
#     direccion = models.CharField(max_length=255)
    
#     # Ubicación geográfica (para integrar mapas)
#     ciudad = models.CharField(max_length=100, blank=True, null=True)
#     estado = models.CharField(max_length=100, blank=True, null=True)
#     pais = models.CharField(max_length=100, blank=True, null=True)
#     latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
#     # Características
#     tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
#     habitaciones = models.PositiveIntegerField(default=0)
#     banos = models.PositiveIntegerField(default=0)
#     area = models.PositiveIntegerField(help_text="Área en metros cuadrados", blank=True, null=True)
    
#     # Relaciones
#     # Relación con la inmobiliaria: usamos el app_label 'inmobiliarias' y el modelo Inmobiliaria.
#     inmobiliaria = models.ForeignKey('inmobiliarias.Inmobiliaria', on_delete=models.CASCADE, related_name='propiedades')
#     # Relación con el agente: usamos 'usuarios.Usuario'. Asegúrate de que AUTH_USER_MODEL esté configurado como 'usuarios.Usuario'
#     agente = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True, related_name='propiedades')
    
#     # Fechas
#     creado_en = models.DateTimeField(auto_now_add=True)
#     actualizado_en = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.titulo
