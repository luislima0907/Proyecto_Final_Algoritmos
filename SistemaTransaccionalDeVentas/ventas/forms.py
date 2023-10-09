from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("codigo", "nombre", "direccion")
        labels = {
            "codigo": "Codigo_cliente: ",
            "nombre": "Nombre_cliente",
            "direccion": "Direccion_cliente",
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("codigo", "nombre", "direccion")
        labels = {
            "codigo": "Codigo_cliente: ",
            "nombre": "Nombre_cliente",
            "direccion": "Direccion_cliente",
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"type": 'text', "id": 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={"id": 'nombre_editar'}),
            'direccion': forms.TextInput(attrs={"id": 'direccion_editar'}),
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("codigo", "nombre", "existencia", "proveedor", "precio", "imagen")
        labels = {
            "codigo": "Cod. Barras: ",
            "nombre": "Nombre del producto",
            "existencia": "Cantidad del producto",
            "proveedor": "Nombre del proveedor",
            "precio": "Costo del producto",
            "imagen": "Imagen de referencia hacia el producto",
        }