from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from Apps.Usuarios.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Pregunta(models.Model):

    categorias = [
        ('Salud','Salud')
        , ('Miscelaneo','Miscelaneo')
        , ('Deportes','Deportes')
        , ('Tecnologia','Tecnologia')
        , ('Cultura','Cultura')
        , ('Educacion','Educacion')

    ]


    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField(null = True ,blank = True)
    Categoria = models.CharField(max_length=10, choices = categorias,null=False,blank=False)
    Autor = models.ForeignKey('User',on_delete=models.CASCADE)
    Fecha =  models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.Titulo

class Respuesta(models.Model):
    Descripcion = models.TextField(null = True ,blank = True)
    Autor = models.ForeignKey('User',on_delete=models.CASCADE)
    Fecha = models.DateField(auto_now=True)
    Pregunta = models.ForeignKey('Pregunta',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return self.Descripcion

def User_img_path(instance,filename):
    return'/'.join(['fotos_perfil/',instance.username+'.jpg'])
class User(AbstractUser):

    mod = [

        (False,"No")
        ,(True,"Si")
    ]

    foto = models.ImageField(upload_to=User_img_path,null=True,blank=True)
    is_moderador = models.BooleanField(default=False,choices = mod,null=False,blank=False)