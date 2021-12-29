from django.db import models
from main.models import Timestamped


class Author(Timestamped):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    is_alive = models.BooleanField(default=True)
    birth_date = models.DateField(blank=True)
    birth_city = models.CharField(max_length=255, blank=True)
    death_date = models.DateField(blank=True)
    death_city = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
