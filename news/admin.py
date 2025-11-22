from django.contrib import admin
from .models import Article, UserReadHistory, Favorite

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source_name', 'published_at', 'created_at']
    list_filter = ['category', 'source_name', 'published_at']
    search_fields = ['title', 'description', 'author']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'published_at'

@admin.register(UserReadHistory)
class UserReadHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'read_at']
    list_filter = ['user', 'read_at']
    search_fields = ['article__title', 'user__username']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'favorited_at']
    list_filter = ['user', 'favorited_at']
    search_fields = ['article__title', 'user__username']