from django.urls import path
from . import views
urlpatterns = [
    path('', views.ventas_views, name='Ventas'),
    path('clientes/', views.clientes_views, name='Clientes'),
    path('add_cliente/', views.add_cliente_views, name='AddCliente'),
    path('edit_cliente/', views.edit_cliente_views, name='EditCliente'),
    path('delete_cliente/', views.delete_cliente_views, name='DeleteCliente'),
    path('productos/', views.productos_views, name='Productos'),
    path('add_producto/', views.add_producto_views, name='AddProducto'),
    path('add_venta/', views.add_ventas.as_views(), name='AddVenta'),
    path('export/', views.export_pdf_views, name='ExportPDF'),
    path('export/<id>/<iva>', views.export_pdf_views, name='ExportPDF'),
]