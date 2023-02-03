from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","published","post_categories")
    ordering = ("author", "published",)
    readonly_fields = ("created", "updated",)
    search_fields = ("title","content","author__username", "categories__name",)
    list_filter = ("categories__name","author__username")

    date_hierarchy = "published"

    def post_categories(self, obj):
        return ", ".join(x.name for x in obj.categories.all().order_by("name"))

    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)