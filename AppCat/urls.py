from django.urls import path
from AppCat.views import *

urlpatterns = [
    path("",inicio, name="Home"),

    path("login/", iniciar_sesion, name="Iniciar Sesion"),
    path("signup/", registro, name="Registrarse"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
    path("edit/", editarPerfil, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contraseña"),
    path("avatar/", agregar_avatar, name="Agregar Avatar")

    path("nuevo_cliente", agregar_Cliente),
    path("nueva_compra",agregar_compra),
    path("crear_presupuesto",agregar_presupuesto),
    path("buscar_cliente", buscar_cliente),
    path("resultadoCli",resultado_busqueda),

    path("ver_compra",ver_compra),
    path("ver_cliente",ver_cliente),
    path("ver_presupuesto",ver_presupuesto),
    
    path("lista_compras/", CompraLista.as_view()),
    path("nuevo_presupuesto/", presupuesto.as_view()),
    path("editar_presupuesto/<int:pk>", PresupuestoEditar.as_view()),
    path("borrar_presupuesto/<int:pk>", presupuestoBorrarBorrar.as_view())
    

]