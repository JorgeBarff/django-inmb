# from django.urls import path
# from .views import home

# urlpatterns = [
#     path('', home, name='home'),
# ]


from django.urls import path
from . import views
from .views import registro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Rutas para recuperación de contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


# urlpatterns = [
#     path('registro/', registro, name='registro'),    
# ]


