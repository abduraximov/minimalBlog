from django.contrib import admin
from apps.post.models import Category, Author, Tag, Post, Video, ViewPost


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(ViewPost)
admin.site.register(Post, ArticleAdmin)
