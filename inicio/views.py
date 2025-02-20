
from django.shortcuts import render, redirect

from django.http import HttpResponse

from inicio.models import Vinos

from inicio.forms import CargarVinos, FiltroVino


def inicio (request):
  
    return render(request, 'inicio/inicio.html')

def cargar_vinos(request):

    formulario = CargarVinos()
    if request.method == "POST":
        formulario = CargarVinos(request.POST)
        if formulario.is_valid():
            print('Cleaned Data:', formulario.cleaned_data)
            
            
            vino = Vinos(
                variedad=formulario.cleaned_data.get('variedad'),
                etiqueta=formulario.cleaned_data.get('etiqueta'),
                descripcion=formulario.cleaned_data.get('descripcion')
            )
            vino.save()
            return redirect("listar_vinos")
    return render(request, 'inicio/cargar_vinos.html', {'formulario': formulario})


  
def listar_vinos(request):
    vinos = Vinos.objects.all()
    return render(request, 'inicio/listar_vinos.html', {'vinos': vinos})

def filtrar_vinos(request):
    form = FiltroVino(request.GET)
    vinos = Vinos.objects.all()  
    
    if form.is_valid():
        variedad = form.cleaned_data.get('variedad')
        if variedad:
            vinos = vinos.filter(variedad__icontains=variedad) 
    
    return render(request, 'inicio/filtrar_vinos.html', {'form': form, 'vinos': vinos})

def detalle_vinos(request, id):
    vino= Vinos.objects.get(id=id)
    return render(request, 'inicio/detalle_vinos.html', {'vino': vino})

def detalle_vinos(request, id):
    vino= Vinos.objects.get(id=id)
    return render(request, 'inicio/detalle_vinos.html', {'vino': vino})

def borrar_vinos(request, id):
    vino= Vinos.objects.get(id=id)
    vino.delete()
    return redirect("listar_vinos")


    