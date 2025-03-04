from django.urls import path
from .views import propiedades_home

urlpatterns = [
  path('', propiedades_home, name='propiedades_home'),
]
