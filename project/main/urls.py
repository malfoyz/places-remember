from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import add_memory, delete_memory, edit_memory, index, logout_view

app_name = 'main'
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('delete/<int:pk>/', delete_memory, name='delete_memory'),
    path('edit/<int:pk>/', edit_memory, name='edit_memory'),
    path('add/', add_memory, name='add_memory'),
    path('', index, name='index'),
]
