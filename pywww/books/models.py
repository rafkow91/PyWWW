from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_first_name = models.CharField(max_length=60)
    author_last_name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    publication_year = models.IntegerField()
    publication_city = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
