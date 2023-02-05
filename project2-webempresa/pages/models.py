from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
  title = models.CharField(verbose_name="Titulo", max_length=200)
  # content = models.TextField(verbose_name="Contenido")
  content = RichTextField(verbose_name="Contenido")
  order = models.SmallIntegerField(verbose_name="Orden", default=0)
  created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
  updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

  class Meta:
    # cambiar como se ve el nombre del model en el admin
    verbose_name="página"
    verbose_name_plural="páginas"
    # orden por defecto
    ordering=['order','title']

  def __str__(self):
    return self.title