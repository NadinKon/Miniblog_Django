from django.contrib import admin
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_displ = ('title', 'autor')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_displ = ('name', 'post')
