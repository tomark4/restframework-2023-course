from django import forms
from .models import Page

class PageForm(forms.ModelForm):

  class Meta:
    model = Page
    fields = ('title','content','order',)
    widgets = {
      'title': forms.TextInput(attrs={"class":"form-control", "placeholder": "Title"}),
      'content': forms.Textarea(attrs={"class":"form-control", "placeholder": "Content"}),
      'order': forms.NumberInput(attrs={"class":"form-control", "placeholder": "Orden"}),
    }

    labels = {
      'title': '',
      'content': '',
      'order': '',
    }