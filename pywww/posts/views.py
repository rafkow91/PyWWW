from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}

    return render(request, 'posts/list.html', context)


def post_details(request, post_id):
    context = {'post': Post.objects.get(id=post_id)}

    return render(request, 'posts/details.html', context)
