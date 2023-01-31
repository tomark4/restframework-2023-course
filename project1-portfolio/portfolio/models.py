from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=255, verbose_name="Titulo")
  description = models.TextField(verbose_name="Descripcion")
  image = models.ImageField(upload_to="projects", verbose_name="Imagen")
  url = models.URLField(blank=True, null=True, verbose_name="Enlace")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado") # auto_now_add Cuando se crea
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado") # auto_now Cada que se actualiza


  class Meta:
    # cambiar como se ve el nombre del model en el admin
    verbose_name="proyecto"
    verbose_name_plural="proyectos"
    # orden por defecto
    ordering=['-created_at']

  def __str__(self):
    return self.title