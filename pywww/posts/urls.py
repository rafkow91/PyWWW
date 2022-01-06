from django.urls import path

from .views import posts_list, post_details, add_post_form, post_edit_details

app_name = 'posts'
urlpatterns = [
    path('<int:post_id>', post_details, name='details'),
    path('<int:post_id>/edit', post_edit_details, name='edit'),
    path('add', add_post_form, name='add'),
    path('', posts_list, name='list'),
]
