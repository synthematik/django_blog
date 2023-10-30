from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/base_blog.html', context={'posts':posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'