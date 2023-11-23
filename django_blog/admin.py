from django.contrib import admin
from blog.models import Post, Tag, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_pub')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment_text', 'post')
