from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Book
from .forms import BookForm


def start_view(request):
    return HttpResponse('<h1>Tu będzie moja biblioteka</h1><p>Więcej już niebawem</p>')


def books_list(request):
    context = {'books_list': Book.objects.all()}

    return render(request, 'books/list.html', context)


def book_details(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}

    return render(request, 'books/details.html', context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            form.helper.form_action = f'/books/{book_id}/edit'
        return HttpResponseRedirect('/books/list')
    else:
        form = BookForm(instance=book)
        if not request.user.is_authenticated:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []
    return render(request, 'books/add.html', {'form': form})


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.helper.form_action = 'books:add'
        return HttpResponseRedirect('/books/list')
    return render(request, 'books/add.html', {'form': form})
