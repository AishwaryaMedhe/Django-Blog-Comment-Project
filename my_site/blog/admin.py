from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Author, Tag, Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter=("title","date","tags")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}


class CommentAdmin(ModelAdmin):
    list_display=("user_name","post")

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
