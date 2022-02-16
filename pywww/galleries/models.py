from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField

from main.models import Timestamped


class StatusChoices(models.Model):
    HIDE = 1
    PUBLISHED = 2
    NEW = 3
    STATUS_CHOICES = [
        (HIDE, 'hide'),
        (PUBLISHED, 'published'),
        (NEW, 'new'),
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=NEW)

    class Meta:
        abstract = True

    @property
    def is_published(self):
        return self.status == StatusChoices.PUBLISHED

    @property
    def is_hide(self):
        return self.status == StatusChoices.HIDE


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        i = 0
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        i += 1
                        slug += f'-{i}'
                    else:
                        break

            self.slug = slug

        return super().save(*args, **kwargs)


def upload_to(instance, filename):
    return f'galleries/{instance.gallery.slug}/{filename}'


class Gallery(Timestamped, StatusChoices, SlugMixin):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == StatusChoices.HIDE:
            Photo.objects.filter(gallery=self.pk).update(status=StatusChoices.HIDE)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Photo(Timestamped, StatusChoices, SlugMixin):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    image = ImageField(upload_to=upload_to)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    source = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title
