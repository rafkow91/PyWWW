from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    exclude = ['author']
    list_display = ['title', 'publication_year', 'publication_city', 'available']
    search_fields = ['title', 'description', 'author_first_name', 'author_last_name']
    list_filter = ['available']
    autocomplete_fields = ('tags',)
    resource_class = BookResource

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
