from django.db import models

# Create your models here.

class Page(models.Model):
  title = models.CharField(verbose_name="Titulo", max_length=200)
  content = models.TextField(verbose_name="Contenido")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
  updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

  class Meta:
    # cambiar como se ve el nombre del model en el admin
    verbose_name="página"
    verbose_name_plural="páginas"
    # orden por defecto
    ordering=['-created']

  def __str__(self):
    return self.title