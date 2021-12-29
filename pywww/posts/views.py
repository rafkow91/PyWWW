from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm


def posts_list(request):
    posts = Post.objects.filter(published=True)

    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)

    context = {'posts_list': posts}

    return render(request, 'posts/list.html', context)


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {}
    if post.published:
        context['post'] = post

    return render(request, 'posts/details.html', context)


def add_post_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            post = Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse("posts:add"))
    else:
        form = PostForm()
    return render(request, 'posts/add.html', {'form': form})
