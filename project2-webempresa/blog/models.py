from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        # cambiar como se ve el nombre del model en el admin
        verbose_name="categoria"
        verbose_name_plural="categorias"
        # orden por defecto
        ordering=['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Publicado el", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        # cambiar como se ve el nombre del model en el admin
        verbose_name="entrada"
        verbose_name_plural="entradas"
        # orden por defecto
        ordering=['-created']

    def __str__(self):
        return self.title