from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto,Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

#@permission_required('JAGUARETE.view_categoria')
def index(request):
    listado_producto=Producto.objects.all()
    categoria= Categoria.objects.all()
    destacados = Producto.objects.all()[:3]
    paginator=Paginator(listado_producto,8)
    pagina=request.GET.get("actual") or 1
    productos=paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)

    return render(request, "JAGUARETE/index.html",{
        "paginas": paginas,
        "pagina_actual": pagina_actual,
        "destacados": destacados,
        "lista_productos":productos,
        "titulo":"Home",
        "categorias": categoria
    })

def busqueda(request, categoria_id):
    iterable = Categoria.objects.get(id=categoria_id)
    categoria = Categoria.objects.all()
    listado_producto = Producto.objects.all()
    return render(request, "JAGUARETE/busqueda.html",{
        "titulo": "busqueda",
        "lista_productos": listado_producto,
        "iterable": iterable,
        "categorias": categoria
    })
def productos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    categoria = Categoria.objects.all()
    return render(request, "JAGUARETE/producto.html",{
        "titulo": "producto",
        "producto": producto,
        "categorias": categoria
    })

#@login_required
def carrito(request):
    categoria = Categoria.objects.all()
    return render(request, "JAGUARETE/carrito.html",{
        "titulo": "carrito",
        "categorias": categoria
    })

def producto(request):
    categoria = Categoria.objects.all()
    return render(request, "JAGUARETE/producto.html",{
        "titulo": "producto",
        "categorias": categoria
    })
def acercaDe(request):
    categoria = Categoria.objects.all()
    return render(request, "JAGUARETE/acercaDe.html",{
        "titulo": "acercaDe",
        "categorias": categoria
    })

