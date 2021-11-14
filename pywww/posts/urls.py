from django.urls import path
from .views import posts_list, post_details

urlpatterns = [
    path('', posts_list),
    path('1', post_details),
]