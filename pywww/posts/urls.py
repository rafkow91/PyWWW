from django.urls import path

from .views import posts_list, post_details

app_name = 'posts'
urlpatterns = [
    path('<int:post_id>', post_details, name='details'),
    path('', posts_list, name='list'),
]
