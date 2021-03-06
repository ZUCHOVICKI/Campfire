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
from Apps.QAs import views as Views_QAs

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # path('',views_UserLog.First,name='First'),
    path('CrearPregunta',Views_QAs.CrearPregunta,name='CrearPregunta'),
    path('HomeQA',Views_QAs.HomeQA,name='HomeQA'),
    path('NuevaPregunta',Views_QAs.NuevaPregunta,name='NuevaPregunta'),
    path('Salud',Views_QAs.Salud,name='Salud'),
    path('Deportes',Views_QAs.Deportes,name='Deportes'),
    path('Cultura',Views_QAs.Cultura,name='Cultura'),
    path('Educacion',Views_QAs.Educacion,name='Educacion'),
    path('Tecnologia',Views_QAs.Tecnologia,name='Tecnologia'),
    path('Misc',Views_QAs.Misc,name='Misc'),
    path('PreguntasYRespuestas/<int:idPregunta>/<Autor>',Views_QAs.PreguntasYRespuestas,name='PreguntasYRespuestas'),
    path('BorrarPregunta',Views_QAs.BorrarPregunta,name='BorrarPregunta'),
    path('NuevaRespuesta',Views_QAs.NuevaRespuesta,name='NuevaRespuesta')
    
]

urlpatterns += staticfiles_urlpatterns()