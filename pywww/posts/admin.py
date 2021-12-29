from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Post


class PostResource(resources.ModelResource):

    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored']
    search_fields = ['title', 'content']
    list_filter = ['published', 'sponsored']
    resource_class = PostResource
