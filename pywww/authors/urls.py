from django.urls import path
from .views import author_details

app_name = 'authors'
urlpatterns = [
    path('<int:author_id>', author_details, name='details'),
]