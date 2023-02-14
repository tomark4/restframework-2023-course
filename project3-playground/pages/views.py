from .models import Page
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm
# from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


"""
decorators utils =>>> login_required, permissions_required
"""

class StaffRequiredMixin(object):
    """
        Mixin para comprobar que el usuario sea staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# listar
class PagesListView(ListView):
    model = Page

# detail
class PageDetailView(DetailView):
    model = Page

# create
@method_decorator(staff_member_required, name="dispatch")
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:list')

    # def dispatch(self, request, *args, **kwargs):
    #     print(request.user)
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy("admin:login"))
    #     return super(PageCreateView, self).dispatch(request, *args, **kwargs)

    # define success url with class method
    # def get_success_url(self):
    #     return reverse('pages:list')

# update
class PageEditView(StaffRequiredMixin, UpdateView):
    model = Page
    # fields = ('title','content','order')
    form_class = PageForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('pages:list')

    def get_success_url(self) -> str:
        return reverse_lazy('pages:update',args=[self.object.pk]) + '?ok'


class PageDeleteView(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:list')
