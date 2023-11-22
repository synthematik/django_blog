from django.urls import path
from .views import profile_view, register_view

urlpatterns = [
    path('', profile_view, name='profile_url'),
    path('register/', register_view, name='register_url'),
]