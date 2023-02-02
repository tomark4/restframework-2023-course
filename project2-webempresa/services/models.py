from django.db import models

# Create your models here.

class Service(models.Model):
  title = models.CharField(max_length=255, verbose_name="Titulo")
  subtitle = models.CharField(max_length=255, verbose_name="Subtitulo")
  content = models.TextField(verbose_name="Contenido")
  image = models.ImageField(upload_to="services", verbose_name="Imagen")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

  class Meta:
    # cambiar como se ve el nombre del model en el admin
    verbose_name="servicio"
    verbose_name_plural="servicios"
    # orden por defecto
    ordering=['-created_at']

  def __str__(self):
    return self.title