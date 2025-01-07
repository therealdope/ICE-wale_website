from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_url', 'image_type', 'list')
    list_filter = ('image_type',)