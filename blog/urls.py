from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='post_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
]