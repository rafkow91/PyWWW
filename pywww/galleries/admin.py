from django.contrib import admin
from django.db import models
from import_export import resources
from import_export.admin import ExportMixin

from main.widgets import AdminImageWidget
from .models import Gallery, Photo


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery


class PhotoInline(admin.StackedInline):
    model = Photo
    fields = ['title', 'image']
    readonly_fields = ['title', 'image']
    extra = 1
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


@admin.register(Gallery)
class GalleryAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['title', 'photos_count', 'is_published']
    fields = ['title', 'slug', 'description', 'status']
    readonly_fields = ['slug']

    inlines = (PhotoInline,)



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    # fields = ['title', 'short_description', 'image', 'status']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
