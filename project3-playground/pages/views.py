from .models import Page
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# listar
class PagesListView(ListView):
    model = Page

# detail
class PageDetailView(DetailView):
    model = Page

# create
class PageCreateView(CreateView):
    model = Page
    fields = ('title','content', 'order')
    success_url = reverse_lazy('pages:list')

    # define success url with class method
    # def get_success_url(self):
    #     return reverse('pages:list')

# update
class PageEditView(UpdateView):
    model = Page
    fields = ('title','content','order')
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('pages:list')

    def get_success_url(self) -> str:
        return reverse_lazy('pages:update',args=[self.object.pk]) + '?ok'


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:list')
