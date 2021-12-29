from django.urls import path
from .views import start_view, books_list, book_details

app_name = 'books'
urlpatterns = [
    path('<int:book_id>', book_details, name='details'),
    path('list', books_list, name='list'),
    path('', start_view, name='home'),
]