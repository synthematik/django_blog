from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.urls import reverse

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


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'post_list_url'