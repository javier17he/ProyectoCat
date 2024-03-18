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

def crear_estudiante(request):

    est_1 = Estudiantes(nombre="Diego", apellido="De La Fuente", email="estudiante@ch.com", edad=28)

    est_2 = Estudiantes(nombre="Belen", apellido="Ulloa", email="estudiante2@ch.com", edad=38)

    est_1.save()
    est_2.save()

    info = {"nombre1":est_1.nombre, "nombre2":est_2.nombre}


    return render(request, "estudiantes/crear_estudiantes.html", info) #1er arg -- request, 2do arg -- template, 3er arg -- contexto(diccionario)

#Con formulario (crear con valores especificos)
@login_required
def crear_nuevo_estudiante(request):

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST,request.FILES) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            estudiante_nuevo = Estudiantes(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                email=info_dic["email"],
                edad=info_dic["edad"],
                profesor=info_dic["profesor"],
                imagen=info_dic["imagen"]
                )
            
            estudiante_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EstudianteFormulario()

    return render(request, "estudiantes/crear_estudiantes.html", {"formu":formulario})


def ver_estudiantes(request):

    todos_estudiantes = Estudiantes.objects.all() #obtener todos los estudiantes que existen

    return render(request, "estudiantes/ver_estudiantes.html", {"total":todos_estudiantes})

@login_required
def actualizar_estudiantes(request, estudiante_info):

    estudiante_elegido = Estudiantes.objects.get(id=estudiante_info)

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            #Cambiado los datos de un objeto que ya se habia creado!!
            estudiante_elegido.nombre = info_dic["nombre"]
            estudiante_elegido.apellido = info_dic["apellido"]
            estudiante_elegido.email = info_dic["email"]
            estudiante_elegido.edad = info_dic["edad"]

            estudiante_elegido.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EstudianteFormulario(initial={"nombre":estudiante_elegido.nombre, "apellido":estudiante_elegido.apellido,"email":estudiante_elegido.email, "edad":estudiante_elegido.edad})

    return render(request, "estudiantes/actualizar_estudiantes.html", {"formu":formulario})

@login_required
def borrar_estudiante(request, estudiante_info):

    estudiante_elegido = Estudiantes.objects.get(id=estudiante_info)

    estudiante_elegido.delete()

    return render(request, "inicio.html")

# CRUD de Cursos

def crear_curso(request):

    if request.method == "POST": #Cuando aprieto el boton de enviar!!!
        
        curso_nuevo = Curso(nombre=request.POST["nombre"],comision=request.POST["comision"])
        #Leer la informacion y guardarla en la base de datos!!!
        curso_nuevo.save()

        return render(request, "inicio.html")

    
    return render(request, "cursos/crear_cursos.html")

@login_required
def ver_cursos(request):

    todos_cursos = Curso.objects.all()

    return render(request, "cursos/ver_cursos.html", {"total":todos_cursos})



def borrar_curso(request, curso_info):

    curso_elegido = Curso.objects.get(id=curso_info)

    curso_elegido.delete()

    return render(request, "inicio.html")


# CRUD de Profesores

def crear_profesor(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            profesor_nuevo = Profesor(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                email=info_dic["email"],
                profesion=info_dic["profesion"]
                )
            
            profesor_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = ProfesorFormulario()

    return render(request, "profes/crear_profesor.html", {"formu":formulario})

def ver_profesores(request):

    return render(request, "profes/ver_profes.html")


#CRUD de Entregables

#Crear un entregable en la base de datos usando un formulario    
def crear_entregable(request):

    if request.method == "POST":

        formulario = EntregableFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            entrega_nueva = Entregable(
                nombre=info_dic["nombre"],
                fechaEntrega=info_dic["fechaEntrega"],
                entregado=info_dic["entregado"]
                )
            
            entrega_nueva.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EntregableFormulario()

    return render(request, "entregas/crear_entregable.html", {"formu":formulario})

def ver_entregables(request):

    return render(request, "entregas/ver_entregables.html")


# Busqueda 

def buscar_curso(request):
    

    if request.GET: #Solo si es que hay una busqueda!!!

        nombre = request.GET["nombre"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        cursos = Curso.objects.filter(nombre__icontains=nombre) #filtrar todos los cursos que tengan dicho nombre!!
        
        mensaje = f"Estamos buscando al curso {nombre}"

        return render(request, "cursos/resultados_cursos.html", {"mensaje":mensaje, "resultados":cursos})

    
    return render(request, "cursos/resultados_cursos.html") #si todavia no hay una busqueda


# Vistas basadas en Clases!!

class CursosLista(ListView):
    model = Curso
    template_name = "cursos/lista_de_cursos.html"

# Create del CRUD
class CursosCrear(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = "cursos/nuevo_curso.html"
    fields = ["nombre", "comision"]
    success_url = "/AppCoder/ver_cursos/"
    

# Update del CRUD
    
class CursosEditar(UpdateView):
    model = Curso
    template_name = "cursos/nuevo_curso.html"
    fields = ["nombre", "comision"]
    success_url = "/AppCoder/"


# Delete del CRUD

class CursosBorrar(DeleteView):
    model = Curso
    template_name = "cursos/borrar_curso.html"
    success_url = "/AppCoder/"


class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "registro/cambiar_contra.html"
    success_url = "/AppCoder/"