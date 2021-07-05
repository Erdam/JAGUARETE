from django.urls import path, include
from . import views

app_name = "USUARIOS"
urlpatterns = [
    path('', views.registro, name="registro"),
]