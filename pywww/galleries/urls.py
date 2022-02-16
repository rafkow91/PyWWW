from django.urls import path
from .views import galleries_list, gallery_details, gallery_add, photo_add

app_name = 'galleries'
urlpatterns = [
    path('', galleries_list, name='galleries'),
    path('<gallery_slug>', gallery_details, name='details'),
    path('add/', gallery_add, name='add_gallery'),
    path('<gallery_slug>/add/', photo_add, name='add_photo'),
]
