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


