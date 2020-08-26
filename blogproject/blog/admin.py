from django.contrib import admin

from .models import Post

# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['created', 'author', 'publish', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    raw_id_fields = ['author']


admin.site.register(Post, PostAdmin)
