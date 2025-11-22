from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """Modelo para armazenar artigos de notícias"""
    
    source_id = models.CharField(max_length=100, null=True, blank=True)
    source_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=1000, unique=True)
    url_to_image = models.URLField(max_length=1000, null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, default='culture')
    
    # Metadados
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
    
    def __str__(self):
        return self.title[:50]


class UserReadHistory(models.Model):
    """Histórico de leitura do usuário"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='read_history')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-read_at']
        verbose_name = 'Histórico de Leitura'
        verbose_name_plural = 'Históricos de Leitura'
        unique_together = ['user', 'article']
    
    def __str__(self):
        return f"{self.user.username} - {self.article.title[:30]}"


class Favorite(models.Model):
    """Notícias favoritas do usuário"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-favorited_at']
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ['user', 'article']
    
    def __str__(self):
        return f"{self.user.username} - {self.article.title[:30]}"