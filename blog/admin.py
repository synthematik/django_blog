from django.contrib import admin
from .models import Post, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_pub')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']