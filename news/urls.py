from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('random/', views.random_news, name='random_news'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('favorite/<int:article_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),
]