from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
  # Obtener todos los proyectos
  projects = Project.objects.all()
  # return HttpResponse(html_base + "<h1>Portfolio</h1>")
  # pasar data a la view con un diccionario conocido como context
  return render(request, "portfolio/portfolio.html",{'projects':projects})
