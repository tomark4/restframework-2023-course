from django.contrib import admin
from .models import Link
# Register your models here.

class SocialAdmin(admin.ModelAdmin):
  readonly_fields = ('created','updated')


  # def get_readonly_fields(self, request, obj=None):
  #   if request.user.groups.filter(name="blog_admin").exists():
  #     return ('created','updated','key','name')

  #   return ('created','updated')
      

admin.site.register(Link, SocialAdmin)
