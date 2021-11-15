# Standard libs
from django.http import HttpResponse
from django.shortcuts import render
# Project's modules
from books.models import Book


def start_view(request):
    return HttpResponse('<h1>Tu będzie moja biblioteka</h1><p>Więcej już niebawem</p>')


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}

    return render(request, 'books/list.html', context)
