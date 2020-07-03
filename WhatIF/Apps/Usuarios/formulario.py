from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
from Apps.Usuarios.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario",max_length=50,min_length=5,required=True,
    widget=forms.TextInput(attrs={'placeholder':'Ingresa Tu usuario'}))
    password = forms.CharField(label="Contraseña",max_length=50,min_length=5,required=True,
    widget=forms.PasswordInput(attrs={'placeholder':'Ingresa Tu contraseña'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name','foto']
        widgets = {
        'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa Tu Username'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingresa una Contraseña'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresa Tu Email'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu Nombre'}),
        'last_name':forms.TextInput(attrs={'placeholder':'Ingresa tu Apellido'}),
        'foto':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ingresa Tu Foto'})
        # 'is_moderador':forms.Select(attrs={'class':'form-control','placeholder':'Eres Artista?'}),

        }
        # 'form-check-label'

        labels={
        
        'foto' : 'FotodePerfil',
        

        }
        help_texts = {
        'username':'Maximo 50 Caracteres',
        'password':'Maximo 8 Caracteres'

        }

