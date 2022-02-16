from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import GalleryForm, PhotoForm
from .models import Gallery, Photo, StatusChoices


def galleries_list(request):
    gallerries = Gallery.objects.filter(status=StatusChoices.PUBLISHED)

    q = request.GET.get('q')
    if q:
        gallerries = gallerries.filter(title__icontains=q)
    if len(gallerries) > 20:
        paginator = Paginator(gallerries, 20)

        page_number = request.GET.get('page')
        gallerries_list = paginator.get_page(page_number)
    else:
        gallerries_list = gallerries

    context = {'galleries_list': gallerries_list}

    return render(request, 'galleries/list.html', context)


def gallery_details(request, gallery_slug):
    gallery = Gallery.objects.get(slug=gallery_slug)
    context = {}
    if gallery.status != StatusChoices.HIDE:
        context['gallery'] = gallery

        photo = Photo.objects.filter(gallery=gallery).filter(status=StatusChoices.PUBLISHED)
        context['photos'] = photo

    return render(request, 'galleries/details.html', context)


def gallery_add(request):
    form = GalleryForm()

    if request.method == "POST":
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/galleries')

    return render(request, 'galleries/add.html', {'form': form})


def photo_add(request, gallery_slug):
    gallery = Gallery.objects.get(slug=gallery_slug)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.gallery = gallery
            instance.save()
            return HttpResponseRedirect(f'/galleries/{gallery_slug}')
    else:
        form = PhotoForm()

    return render(request, 'galleries/add.html', {'form': form, 'gallery': gallery})


