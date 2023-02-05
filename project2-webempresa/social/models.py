from django.db import models

# Create your models here.

class Link(models.Model):
  key = models.SlugField(verbose_name="nombre clave", max_length=100, unique=True)
  name = models.CharField(verbose_name="red social", max_length=200)
  url = models.URLField(verbose_name="enlace", max_length=200, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
  updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

  class Meta:
    # cambiar como se ve el nombre del model en el admin
    verbose_name="enlace"
    verbose_name_plural="enlaces"
    # orden por defecto
    ordering=['name']

  def __str__(self):
    return self.name