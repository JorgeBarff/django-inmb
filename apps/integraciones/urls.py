from django.urls import path
from .views import integraciones_home


urlpatterns = [
    path('', integraciones_home, name='integraciones_home'),
]
