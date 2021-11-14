# Standard libs
from django.shortcuts import render
# Project's files
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}

    return render(request, 'posts/list.html', context)


def post_details(request):
    context = {'post': Post.objects.get(id=1)}

    return render(request, 'posts/details.html', context)
