# equipos/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('equipo/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipo/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipo/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
]