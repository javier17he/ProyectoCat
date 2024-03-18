from django.shortcuts import render
from AppCat.forms import *
from AppCat.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request,"AppCat/inicio.html")

@login_required
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

@login_required
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

@login_required
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

def resultado_busqueda(request):
    cliente = request.GET.get("Nombre Cliente")

    nombre = Cliente.object.filter(nombre_icontains=cliente)

    return render(request, "AppCat/resultadoBusqueda.html", {"nombre":nombre})

def iniciar_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])

            if usuario is not None: #que el usuario existe!!!

                login(request, usuario)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        
            
        else:

            return render(request, "inicio.html", {"mensaje":"Credenciales Incorrectas"})
        
    else:

        formulario = AuthenticationForm()

    return render(request, "registro/inicio_sesion.html", {"formu":formulario})

# Agregar Avatar
@login_required
def agregar_avatar(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=info["imagen"])

            nuevo_avatar.save()
            return render(request, "inicio.html", {"mensaje":"Has creado tu avatar"})
    
    else:

        formulario = AvatarFormulario()


    return render(request, "registro/nuevo_avatar.html", {"formu":formulario})

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user #cual es el usuario que tiene la sesion activa

    if request.method == 'POST':

        miFormulario = EditarUsuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = EditarUsuario(initial={'username':usuario.username, 'first_name':usuario.first_name,
                                                'last_name':usuario.last_name, 'email': usuario.email})


    return render(request, "registro/editar_usuario.html", {"formu":miFormulario})


def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje":"Has cerrado sesión con éxito."})


def ver_presupuesto(request):

    todos_presupuesto = presupuesto.objects.all() #obtener todos los estudiantes que existen

    return render(request, "ver_presupuesto.html", {"total":todos_presupuesto})

@login_required
def actualizar_presupuesto(request, presupuesto):

    presupuesto_elegido = presupuesto.objects.get(id=presupuesto)

    if request.method == "POST":

        formulario = presupuestoForm(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            #Cambiado los datos de un objeto que ya se habia creado!!
            presupuesto_elegido.nombre = info_dic["nombre"]
            presupuesto_elegido.precio = info_dic["precio"]
            presupuesto_elegido.direccion = info_dic["direccion"]
            presupuesto_elegido.producto = info_dic["producto"]
            presupuesto_elegido.cliente = info_dic["cliente"]


            presupuesto_elegido.save()

            return render(request, "inicio.html")
        
    else:

        formulario = presupuestoForm(initial={"nombre":presupuesto_elegido.nombre, "precio":presupuesto_elegido.precio,"direccion":presupuesto_elegido.direccion, "producto":presupuesto_elegido.producto,"cliente":presupuesto_elegido.cliente })

    return render(request, "estudiantes/actualizar_presupuesto.html", {"formu":formulario})

@login_required
def borrar_presupuesto(request, presupuesto_info):

    presupuesto_elegido = presupuesto.objects.get(id=presupuesto_info)

    presupuesto.delete()

    return render(request, "inicio.html")

@login_required
def ver_compra(request):

    todos_compra = Compra.objects.all()

    return render(request, "cursos/ver_compra.html", {"total":todos_compra})

def borrar_presupuesto(request, presupuesto_info):

    presupuesto_elegido = Compra.objects.get(id=presupuesto_info)

    presupuesto_elegido.delete()

    return render(request, "inicio.html")

def ver_cliente(request):

    return render(request, "ver_client.html")

class CompraLista(ListView):
    model = Compra
    template_name = "lista_de_compras.html"

class CompraCrear(LoginRequiredMixin, CreateView):
    model = Compra
    template_name = "nueva_compra.html"
    fields = ["nombre_fiesta", "cliente"]
    success_url = "/AppCat/ver_compra/"

class PresupuestoEditar(UpdateView):
    model = presupuesto
    template_name = "crear_presupuesto.html"
    fields = ["nombre", "cliente"]
    success_url = "/AppCoder/"

class presupuestoBorrar(DeleteView):
    model = presupuesto
    template_name = "borrar_presupuesto.html"
    success_url = "/AppCat/"

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "registro/cambiar_contra.html"
    success_url = "/AppCat/"