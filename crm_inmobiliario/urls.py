"""
URL configuration for crm_inmobiliario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar `include`
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     # Incluir las rutas de las aplicaciones
#     path('usuarios/', include('apps.usuarios.urls')),
#     path('inmobiliarias/', include('apps.inmobiliarias.urls')),
#     path('propiedades/', include('apps.propiedades.urls')),
#     path('integraciones/', include('apps.integraciones.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('apps.usuarios.urls')),  # <- Agrega esto para la página principal
    path('usuarios/', include('apps.usuarios.urls')),
    
    path('inmobiliarias/', include('apps.inmobiliarias.urls')),
    path('propiedades/', include('apps.propiedades.urls')),
    path('integraciones/', include('apps.integraciones.urls')),
]

# Permitir servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







