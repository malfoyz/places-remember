from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import add_memory, index, logout_view

app_name = 'main'
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('add/', add_memory, name='add_memory'),
    path('', index, name='index'),
]
