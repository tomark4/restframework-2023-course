from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

    # extender el diccionario de contexto
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = "Hello world"
    #     return context

    def get(self, request, *args, **kargs):
        return render(request, self.template_name, {'message': 'Hello world!'})

class SampleView(TemplateView):
    template_name = 'core/sample.html'