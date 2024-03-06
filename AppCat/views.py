from django.shortcuts import render
from AppCat.forms import *
from AppCat.models import *


def inicio(request):
     return render(request,"AppCat/inicio.html")

def agregar_Cliente(request):
    if request.method =="POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            info_dict =  formulario.cleaned_data
            nuevo_clienete = Cliente(nombre = info_dict["nombre"],edad = info_dict["edad"], direccion=info_dict["direccion"])
            nuevo_clienete.save()
            return render(request,"inicio.html")
    else:
        formulario = ClienteForm()
    
    return render(request, "AppCat/nuevo_cliente.html",{"form":formulario})
    

def agregar_presupuesto(request):
    if request.method =="POST":
        formulario = presupuestoForm(request.POST)
        if formulario.is_valid():
            info_dict =  formulario.cleaned_data
            nuevo_presupuesto = presupuestoForm(nombre = info_dict["nombre"],precio = info_dict["precio"], direccion=info_dict["direccion"], producto = info_dict["producto"],cliente=info_dict["cliente"])
            nuevo_presupuesto.save()
            return render(request,"inicio.html")
    else:
        formulario = presupuestoForm()
    
    return render(request, "AppCat/crear_presupuesto.html",{"form":formulario})

def agregar_compra(request):
    if request.method =="POST":
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            info_dict =  formulario.cleaned_data
            nuevo_presupuesto = CompraForm(nombreFiesta = info_dict["nombreFiesta"],fecha = info_dict["fecha"], direccion=info_dict["direccion"], producto = info_dict["producto"],cliente=info_dict["cliente"])
            nuevo_presupuesto.save()
            return render(request,"inicio.html")
    else:
        formulario = CompraForm()
    
    return render(request, "AppCat/nueva_compra.html",{"form":formulario})


def buscar_cliente(request):

    return render(request,"AppCat/buscar_cliente.html")
