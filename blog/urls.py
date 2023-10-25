from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list)
]