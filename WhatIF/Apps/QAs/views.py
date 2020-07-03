from django.shortcuts import render , HttpResponse , redirect

from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from Apps.Usuarios.models import User
from Apps.Usuarios.models import Pregunta
from Apps.Usuarios.models import Respuesta
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def CrearPregunta(request):
    return render(request,"CrearPregunta.html")
@login_required
def HomeQA(request):
    preguntas = Pregunta.objects.all().order_by("-Fecha")
    print(preguntas)
    return render(request,"Menu.html",{
        'Preguntas':preguntas
    })

@login_required
def PreguntasYRespuestas(request,idPregunta,Autor):

    preguntas = Pregunta.objects.get(id = idPregunta)
    respuestas = Respuesta.objects.filter(Pregunta_id =idPregunta)
    
    user = User.objects.get(username=Autor)
    print(request.user)
    print(Pregunta.objects.get(id=idPregunta).Autor)
    if request.user == Pregunta.objects.get(id=idPregunta).Autor:
        eliminar = True
    else:
        eliminar=False
    print(eliminar)
    return render(request,"Pregunta.html",{

        'preguntas':preguntas,
        'respuestas':respuestas,
        'idPregunta':idPregunta,
        'user':user,
        'eliminar':eliminar
        
        
    })

@login_required
def NuevaRespuesta(request):
    descripcionRespuesta = request.POST['DescripcionPregunta']
    # AutorRespuesta = request.POST['AutorRespuesta']
    PreguntaRespuesta = request.POST['PreguntaRespuesta']
    pregunta = Pregunta.objects.get(id=PreguntaRespuesta)
    
    try:
        
        Respuesta.objects.create(
         Descripcion = descripcionRespuesta,
         Autor = request.user,
         Pregunta = pregunta
        )
        print("HOLA")
        return HttpResponse(True)
    except Exception as error:
        print(error)
        
        return HttpResponse(False)

@login_required
def BorrarPregunta(request):
    idPregunta = request.POST['ID']
    

   

    try:
        pregunta = Pregunta.objects.get(id=idPregunta)

        pregunta.delete()
        return HttpResponse(True)
    except Exception as identifier:
        print(identifier)
        return HttpResponse(False)


@login_required
def NuevaPregunta(request):
    Titulo = request.POST['Titulo']
    Descripcion =  request.POST['Descripcion']
    Categoria =  request.POST['Categoria']

    try:
        pregunta = Pregunta.objects.create(
            Titulo= Titulo,
            Descripcion= Descripcion,
            Categoria= Categoria ,
            Autor= request.user

        )

        
        return HttpResponse(True)
    except Exception as identifier:
        print(identifier)
        return HttpResponse(False)


@login_required
def Salud(request):
    preguntas = Pregunta.objects.filter(Categoria='Salud').order_by("-Fecha")
    print(preguntas)
    return render(request,"Salud.html",{
        'Preguntas':preguntas
    })
@login_required
def Deportes(request):
    preguntas = Pregunta.objects.filter(Categoria='Deportes').order_by("-Fecha")
    print(preguntas)
    return render(request,"Deportes.html",{
        'Preguntas':preguntas
    })
@login_required
def Cultura(request):
    preguntas = Pregunta.objects.filter(Categoria='Cultura').order_by("-Fecha")
    print(preguntas)
    return render(request,"Cultura.html",{
        'Preguntas':preguntas
    })
@login_required
def Educacion(request):
    preguntas = Pregunta.objects.filter(Categoria='Educacion').order_by("-Fecha")
    print(preguntas)
    return render(request,"Educacion.html",{
        'Preguntas':preguntas
    })
@login_required
def Tecnologia(request):
    preguntas = Pregunta.objects.filter(Categoria='Tecnologia').order_by("-Fecha")
    print(preguntas)
    return render(request,"Tecnologia.html",{
        'Preguntas':preguntas
    })
@login_required
def Misc(request):
    preguntas = Pregunta.objects.filter(Categoria='Misc').order_by("-Fecha")
    print(preguntas)
    return render(request,"Misc.html",{
        'Preguntas':preguntas
    })