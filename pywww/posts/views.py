from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm


def posts_list(request):
    posts = Post.objects.filter(published=True)

    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)

    paginator = Paginator(posts, 20)

    page_number = request.GET.get('page')
    post_list = paginator.get_page(page_number)

    context = {'post_list': post_list}

    return render(request, 'posts/list.html', context)


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {}
    if post.published:
        context['post'] = post

    return render(request, 'posts/details.html', context)


def add_post_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            form.helper.form_action = 'posts:add'
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()
    return render(request, 'posts/add.html', {'form': form})


def post_edit_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            form.save_m2m()
            form.helper.form_action = f'/books/{post_id}/edit'
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm(instance=post)
        if not request.user.is_authenticated:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []
    return render(request, 'posts/add.html', {'form': form})
