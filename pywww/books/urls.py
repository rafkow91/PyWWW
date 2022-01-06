from django.urls import path
from .views import start_view, books_list, book_details, add_book, edit_book

app_name = 'books'
urlpatterns = [
    path('<int:book_id>', book_details, name='details'),
    path('<int:book_id>/edit', edit_book, name='edit'),
    path('add', add_book, name='add'),
    path('list', books_list, name='list'),
    path('', start_view, name='home'),
]