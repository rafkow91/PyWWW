from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'publication_city', 'available']
    list_filter = ['available']
    search_fields = ['title', 'description', 'author_first_name', 'author_last_name']
    resource_class = BookResource

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
