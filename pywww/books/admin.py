from django.contrib import admin
from .models import Book


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_first_name', 'author_last_name', 'publication_year', 'publication_city',
                    'created_at', 'modified_at', 'available']
    list_filter = ['available']
    search_fields = ['title', 'description', 'author_first_name', 'author_last_name']
