"""DJANGOA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Apps.Usuarios import views as Views_Usuarios

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',Views_Usuarios.Home,name='Home'),
    path('Login',Views_Usuarios.logIN,name='Login'),
    path('Perfil',Views_Usuarios.Perfil,name='Perfil'),
    path('CambioContraseña',Views_Usuarios.CambioContraseña,name='CambioContraseña'),
    path('Cambiofoto',Views_Usuarios.Cambiofoto,name='Cambiofoto'),
    path('cerrarSesion',Views_Usuarios.cerrarSesion,name='cerrarSesion'),
    path('Registro',Views_Usuarios.Registro,name='Registro'),
]

urlpatterns += staticfiles_urlpatterns()