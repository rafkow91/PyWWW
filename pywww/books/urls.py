from django.urls import path
from .views import start_view, books_list

urlpatterns = [
    path('', start_view),
    path('list', books_list),
]