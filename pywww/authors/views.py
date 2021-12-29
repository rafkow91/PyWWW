from django.shortcuts import render

from .models import Author


def author_details(request, author_id):
    context = {'author': Author.objects.get(id=author_id)}

    return render(request, 'authors/details.html', context)
