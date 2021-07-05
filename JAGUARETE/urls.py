from django.urls import path
from . import views

app_name="url"
urlpatterns = [
    path('', views.index, name="index"),
    path('acercaDe', views.acercaDe, name="acercaDe"),
    path('carrito', views.carrito, name="carrito"),
    path('producto', views.producto, name="producto"),
    path('productos/<int:producto_id>', views.productos, name="productos"),
    path('<int:categoria_id>', views.busqueda, name="busqueda")
]
