from django.contrib import admin
from ventas.models import Cliente, Producto
# Register your models here.

class cliente_admin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "direccion")
    search_fields = ["nombre"]
    readonly_fields = ("created", "updated")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, cliente_admin)

class producto_admin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "imagen", "existencia", "proveedor", "precio")
    search_fields = ["codigo"]
    readonly_fields = ("created", "updated")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, producto_admin)