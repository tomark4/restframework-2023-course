from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.

def contact_view(request):
  contact_form = ContactForm()

  if request.method == 'POST':
    # rellenar el formulario con los campos de la request
    contact_form = ContactForm(data=request.POST)

    # regresa true
    if contact_form.is_valid():
      name = request.POST.get('name','')
      email = request.POST.get('email','')
      message = request.POST.get('message','')
      # send email here or save to database

      # redirect a la pagina si todo marcha bien
      return redirect(reverse('contact')+'?ok')

  return render(request, 'contact/index.html', {'form':contact_form})
