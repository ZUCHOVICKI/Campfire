from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets + (
        ('Campos Extra', {
            'fields':('foto',
            'is_moderador'
            
            )
        }),



    )
# Register your models here.
admin.site.register(User,UsuarioAdmin)
admin.site.register(Pregunta)
admin.site.register(Respuesta)