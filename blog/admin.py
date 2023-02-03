from django.contrib import admin

from .models import Post, Category, Comment


class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInLine]
    prepopulated_fields = {'slug': ('title',)}  # automatically create slugs

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}  # automatically create slugs


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)