from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'core/home.html')

def about(request):
  return render(request, 'core/about.html')

def services(request):
  return render(request, 'core/services.html')

def find_us(request):
  return render(request, 'core/find_us.html')

def contact(request):
  return render(request, 'core/contact.html')

def blog(request):
  return render(request, 'core/blog.html')

def sample_page(request):
  return render(request, 'core/sample_page.html')