from django.db import models
from main.models import Timestamped
from sorl.thumbnail import ImageField


class Author(Timestamped):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True)
    birth_year = models.IntegerField(blank=True)
    birth_city = models.CharField(max_length=255, blank=True)
    death_year = models.IntegerField(blank=True, null=True)
    death_city = models.CharField(max_length=255, blank=True, null=True)
    portrait = ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(Timestamped):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name='books', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    publication_year = models.IntegerField(blank=True)
    publication_city = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name='books', blank=True)
    cover = ImageField(upload_to='books/covers/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
