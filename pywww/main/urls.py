from django.urls import path
from .views import home, about

app_name = 'main'
urlpatterns = [
    path('about', about, name='about'),
    path('', home, name='home'),
]
