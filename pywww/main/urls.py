from django.urls import path

from .views import home, about, contact, userprofile

app_name = 'main'
urlpatterns = [
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_id>/profile', userprofile, name='userprofile'),
    path('', home, name='home'),
]
