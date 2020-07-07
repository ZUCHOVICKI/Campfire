
from django.shortcuts import render , HttpResponse , redirect
from .formulario import LoginForm,RegisterForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from Apps.Usuarios.models import User , Pregunta
from Apps.QAs import views as views_QAs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
# Create your views here.


def Home(request):

    if(request.user.is_authenticated):
        return redirect(views_QAs.HomeQA)
       

        
    else:
        return render(request,'WelcomeHome.html')
    
 
def logIN(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                return redirect(views_QAs.HomeQA)
            else:
                form.add_error(None,'Datos Incorrectos ==> Revisa tus datos')
                # form = LoginForm()

                return render(request,'LogIn.html',{'form':form})


        else:
            return HttpResponse('Revisa tu formulario')
    else:
        form = LoginForm()

        return render(request,'LogIn.html',{'form':form})


def Registro(request):
    print("HOLA MUNDO")
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES,initial={'foto': 'fotos_perfil/camping.png' })

        if form.is_valid():
            username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            Nombre = form.cleaned_data['first_name']
            Apellido = form.cleaned_data['last_name']
            
            foto = form.cleaned_data['foto']
            # is_moderador  =form.cleaned_data['is_moderador']

            user = User.objects.filter(username=username)
            emailUser = User.objects.filter(email=email)

            # print(len(password))
            # if(len(password)<5):
            #     form.add_error('email','Contraseña Invalida')
            #     return render(request,'Registro.html',{'form':form})
            
            if(len(user)>0):
                form.add_error('username','Usuario no Disponible / Ya Registrado')
                return render(request,'Registro.html',{'form':form})
                

            if(len(emailUser)>0):
                form.add_error('email','Correo no Disponible / Ya Registrado ')
                return render(request,'Registro.html',{'form':form})
                
            

            user = User(
                username = username,
                email = email,
                first_name = Nombre,
                last_name = Apellido,
                foto = foto,
                # is_moderador = is_moderador
            )
            user.set_password("id_password1")  
            user.save()
            messages.success(request,'Usuario Creado Exitosamente')
            return render(request,'Registro.html',{'form':form})
            
        else:
            return render(request,'Registro.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'Registro.html',{'form':form})

@login_required
def Perfil(request):
    User = request.user
    preguntas = Pregunta.objects.filter(Autor = request.user).order_by('-Fecha')

    return render(request,'Perfil.html',{'User':User,'Preguntas':preguntas})

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect(Home)
    


def CambioContraseña(request):

    Contraseña  = request.POST['Contraseña']

    

    try:
        User = request.user

        User.set_password(Contraseña)
        User.save()
        login(request,User)
        return HttpResponse(True)
    except Exception as identifier: 
        print(identifier)
        return HttpResponse(False)

def Cambiofoto(request):
    
    Foto = request.FILES['Foto']

    try:
        Userf = request.user
        Userf.foto = Foto
                
            
        
        Userf.save()
        
        return HttpResponse(True)
    except Exception as identifier: 
        print(identifier)
        return HttpResponse(False)