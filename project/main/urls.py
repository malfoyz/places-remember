from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import index, logout_view

app_name = 'main'
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', index, name='index'),
]
