from django.contrib import admin
from django.db import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from main.widgets import AdminImageWidget
from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class BookInline(admin.StackedInline):
    model = Book
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    exclude = ['author']
    list_display = ['title', 'publication_year', 'publication_city', 'available']
    search_fields = ['title', 'description']
    list_filter = ['available']
    autocomplete_fields = ('tags', 'authors')

    resource_class = BookResource

    fields = ['title', 'authors', 'cover', 'description', 'available', 'publication_year', 'publication_city',
              'language', 'tags']

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'birth_year', 'death_year', 'books_count']
    search_fields = ['first_name', 'last_name']

    fields = ['first_name', 'last_name', 'portrait', 'bio', 'birth_year', 'birth_city', 'death_year',
              'death_city']
    raw = (BookInline,)
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
