from django.shortcuts import render
from django.http import HttpResponse
from BlogFinal.models import Carniceria, Verduleria, Panaderia
from BlogFinal.forms import CrearCarniceriaForm, CrearPanaderiaForm, CrearVerduleriaForm

def index(request):
    return render(request, 'BlogFinal/Templates/BlogFinal/inicio.html')

def mostrar_carniceria(request):
    return render(request, 'BlogFinal/Templates/BlogFinal/carniceria.html')

def mostrar_verduleria(request):
    return render(request, 'BlogFinal/Templates/BlogFinal/verduleria.html')

def mostrar_panaderia(request):
    return render(request, 'BlogFinal/Templates/BlogFinal/panaderia.html')

def mostrar_comercio(request):
    return render(request, 'BlogFinal/Templates/BlogFinal/comercios.html')

def crear_carniceria(request):

    if request.method == 'POST':

        formulario = CrearCarniceriaForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            carniceria = Carniceria(nombre = formulario_limpio['nombre'], calle = formulario_limpio['calle'], altura = formulario_limpio['altura'], localidad = formulario_limpio['localidad'], telefono = formulario_limpio['telefono'])

            carniceria.save()

            return render(request, 'carniceria.html')

    else:
        formulario = CrearCarniceriaForm()

    return render(request, 'BlogFinal/templates/BlogFinal/crear_carniceria.html', {'formulario': formulario})


def crear_verduleria(request):

    if request.method == 'POST':

        formulario1 = CrearVerduleriaForm(request.POST)

        if formulario1.is_valid():

            formulario1_limpio = formulario1.cleaned_data

            verduleria = Verduleria(nombre = formulario1_limpio['nombre'], calle = formulario1_limpio['calle'], altura = formulario1_limpio['altura'], localidad = formulario1_limpio['localidad'], telefono = formulario1_limpio['telefono'])

            verduleria.save()

            return render(request, 'verduleria.html')

    else:
        formulario1 = CrearVerduleriaForm()

    return render(request, 'BlogFinal/templates/BlogFinal/crear_verduleria.html', {'formulario1': formulario1})

def crear_panaderia(request):

    if request.method == 'POST':

        formulario2 = CrearPanaderiaForm(request.POST)

        if formulario2.is_valid():

            formulario2_limpio = formulario2.cleaned_data

            panaderia = Panaderia(nombre = formulario2_limpio['nombre'], calle = formulario2_limpio['calle'], altura = formulario2_limpio['altura'], localidad = formulario2_limpio['localidad'], telefono = formulario2_limpio['telefono'])

            panaderia.save()

            return render(request, 'panaderia.html')

    else:
        formulario2 = CrearPanaderiaForm()

    return render(request, 'BlogFinal/templates/BlogFinal/crear_panaderia.html', {'formulario2': formulario2})


def buscar_carniceria(request):

    if request.GET.get('Nombre', False):
        nombre = request.GET["Nombre"]

        carnicerias = Carniceria.objects.filter(nombre__icontains=nombre)

        return render(request, 'BlogFinal/templates/BlogFinal/showing.html', {"carniceria":carnicerias, "Nombre":nombre})
    else:
        respuesta = "No se encontro la carnicería buscada"

    return HttpResponse(respuesta)

def buscar_verduleria(request):

    if request.GET.get('Nombre', False):
        nombre = request.GET["Nombre"]

        verdulerias = Verduleria.objects.filter(nombre__icontains=nombre)

        return render(request, 'BlogFinal/templates/BlogFinal/showing.html', {"carniceria":verdulerias, "Nombre":nombre})
    else:
        respuesta = "No se encontro la verduleria buscada"

    return HttpResponse(respuesta)

def buscar_panaderia(request):

    if request.GET.get('Nombre', False):
        nombre = request.GET["Nombre"]

        panaderias = Panaderia.objects.filter(nombre__icontains=nombre)

        return render(request, 'BlogFinal/templates/BlogFinal/showing.html', {"carniceria":panaderias, "Nombre":nombre})
    else:
        respuesta = "No se encontro la panaderia buscada"

    return HttpResponse(respuesta)