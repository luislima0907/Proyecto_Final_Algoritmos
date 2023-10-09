from django.urls import path
from . import views
urlpatterns = [
    path('', views.inventarios_views, name='Inventarios'),
]