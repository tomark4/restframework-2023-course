from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'core/home.html')

def about(request):
  return render(request, 'core/about.html')

def find_us(request):
  return render(request, 'core/find_us.html')

def contact(request):
  return render(request, 'core/contact.html')

def sample_page(request):
  return render(request, 'core/sample_page.html')