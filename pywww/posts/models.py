from django.db import models
from main.models import Timestamped

class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('tags.Tag', related_name='posts', blank=True)
    image_file = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.title}'
