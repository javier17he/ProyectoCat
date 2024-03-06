from django.urls import path
from AppCat.views import *

urlpatterns = [
    path("nuevo_cliente", agregar_Cliente),
    path("nueva_compra",agregar_compra),
    path("crear_presupuesto",agregar_presupuesto),
    path("buscar_cliente", buscar_cliente),
    path("resultadoCli",resultado_busqueda),
    path("",inicio, name="Home"),
 ]