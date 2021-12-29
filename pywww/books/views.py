from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def start_view(request):
    return HttpResponse('<h1>Tu będzie moja biblioteka</h1><p>Więcej już niebawem</p>')


def books_list(request):
    context = {'books_list': Book.objects.all()}

    return render(request, 'books/list.html', context)


def book_details(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}

    return render(request, 'books/details.html', context)
