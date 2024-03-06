from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    direccion = forms.CharField (max_length=100)
    


class CompraForm(forms.Form):
    fecha = forms.DateField()
    productos =forms.CharField()
    direccion = forms.CharField (max_length=100)
    nombreFiesta = forms.CharField(max_length=50)
    cliente = forms.CharField(max_length=50)

    
class presupuestoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    productos = forms.CharField(max_length=500)
    direccion = forms.CharField(max_length=100)
    cliente = forms.CharField(max_length=50)

