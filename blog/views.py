from django.shortcuts import render
from .models import Post, Tag

def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/base_blog.html', context={'posts':posts})

def post_detail(request, slug):
    posts = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'posts':posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})