from django.urls import path
from .views import inmobiliarias_home

urlpatterns = [
    path('', inmobiliarias_home, name='inmobiliarias_home'),
]
