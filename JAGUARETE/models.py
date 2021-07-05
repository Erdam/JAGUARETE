from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=120, default="")

    def __str__(self):
       return f"{self.nombre}"

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="_img", null=True)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.id }:  {self.titulo}"