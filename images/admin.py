from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Register Image model in Django admin panel
    """
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
