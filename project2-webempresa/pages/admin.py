from django.contrib import admin
from .models import Page
# Register your models here.

class PagesAmdin(admin.ModelAdmin):
  list_display = ('title','order')
  readonly_fields = ('created','updated')

admin.site.register(Page, PagesAmdin)
