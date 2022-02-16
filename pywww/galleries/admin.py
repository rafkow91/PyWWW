from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Gallery, Photo


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery


@admin.register(Gallery)
class GalleryAdmin(ExportMixin, admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

