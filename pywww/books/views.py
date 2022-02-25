from dal import autocomplete
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookForm, AuthorForm, AuthorFormSet
from .models import Book, Author


def start_view(request):
    return HttpResponse('<h1>Tu będzie moja biblioteka</h1><p>Więcej już niebawem</p>')


def books_list(request):
    context = {'books_list': Book.objects.all()}

    return render(request, 'books/list.html', context)


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    book_authors = list(book.authors.all()),

    context = {
        'book': book,
        # 'book_authors': book_authors,
    }

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
    formset = AuthorFormSet(queryset=Author.objects.none())

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        formset = AuthorFormSet(request.POST)
        if form.is_valid():
            instance = form.save()
            if formset.is_valid():
                for f in formset.cleaned_data:
                    if f:
                        author, _ = Author.objects.get_or_create(**f)
                        if author not in instance.authors.all():
                            instance.authors.add(author)
                    instance.save()

        return HttpResponseRedirect('/books/list')
    return render(
        request=request,
        template_name='books/add.html',
        context={
            'form': form,
            'formset': formset,
        }
    )


def add_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.helper.form_action = 'books:add_author'
        return HttpResponseRedirect('/books/list')
    return render(request, 'books/add.html', {'form': form})


class AuthorsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Author.objects.none()

        qs = Author.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
