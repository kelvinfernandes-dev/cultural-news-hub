from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from .models import Article, Favorite
from .services import NewsAPIService
from django.shortcuts import redirect
from django.contrib import messages
import random


def home(request):
    """View principal - mostra notícias de cultura por tema"""
    
    # Pega o tema selecionado (padrão: todos)
    selected_theme = request.GET.get('theme', 'todos')
    
    # Lista de temas disponíveis
    themes = [
        {'code': 'todos', 'name': 'Todos', 'icon': '🌐', 'color': 'gray'},
        {'code': 'cinema', 'name': 'Cinema', 'icon': '🎬', 'color': 'red'},
        {'code': 'musica', 'name': 'Música', 'icon': '🎵', 'color': 'purple'},
        {'code': 'arte', 'name': 'Arte', 'icon': '🎨', 'color': 'pink'},
        {'code': 'literatura', 'name': 'Literatura', 'icon': '📚', 'color': 'blue'},
        {'code': 'teatro', 'name': 'Teatro', 'icon': '🎭', 'color': 'indigo'},
        {'code': 'games', 'name': 'Games', 'icon': '🎮', 'color': 'green'},
        {'code': 'tv', 'name': 'TV & Séries', 'icon': '📺', 'color': 'orange'},
    ]
    
    # Busca notícias do banco
    if selected_theme == 'todos':
        articles = Article.objects.all().order_by('-published_at')
    else:
        articles = Article.objects.filter(category=selected_theme).order_by('-published_at')
    
    # Se não tiver notícias OU forçar fetch, busca da API
    force_fetch = request.GET.get('fetch', False)
    
    if (not articles.exists() or force_fetch) and selected_theme != 'todos':
        service = NewsAPIService()
        articles_list = service.fetch_news_by_theme(theme=selected_theme, page_size=30)
        
        # Recarrega do banco
        if selected_theme == 'todos':
            articles = Article.objects.all().order_by('-published_at')
        else:
            articles = Article.objects.filter(category=selected_theme).order_by('-published_at')
    
    # Pega uma notícia aleatória para destacar
    featured_article = None
    if articles.exists():
        featured_article = random.choice(articles[:20])  # Escolhe entre as 20 mais recentes
    
    # Pega as outras notícias (excluindo a destacada)
    other_articles = articles.exclude(id=featured_article.id) if featured_article else articles
    
    context = {
        'featured_article': featured_article,
        'articles': other_articles[:12],
        'themes': themes,
        'selected_theme': selected_theme,
    }
    
    return render(request, 'news/home.html', context)

@require_http_methods(["GET"])
def random_news(request):
    """Retorna uma notícia aleatória (AJAX)"""
    
    articles = Article.objects.filter(category='culture')
    
    # Se tiver menos de 5 notícias, busca mais da API
    if articles.count() < 5:
        service = NewsAPIService()
        service.fetch_culture_news()
        articles = Article.objects.filter(category='culture')
    
    if articles.exists():
        article = random.choice(articles)
        
        data = {
            'id': article.id,
            'title': article.title,
            'description': article.description,
            'url': article.url,
            'url_to_image': article.url_to_image,
            'source_name': article.source_name,
            'published_at': article.published_at.strftime('%d/%m/%Y'),
            'author': article.author or 'Desconhecido'
        }
        
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Nenhuma notícia encontrada'}, status=404)


def article_detail(request, article_id):
    """View de detalhes da notícia"""
    
    article = get_object_or_404(Article, id=article_id)
    
    # Se o usuário estiver logado, salva no histórico
    if request.user.is_authenticated:
        from .models import UserReadHistory
        UserReadHistory.objects.get_or_create(
            user=request.user,
            article=article
        )
    
    context = {
        'article': article,
    }
    
    return render(request, 'news/article_detail.html', context)


@require_http_methods(["POST"])
def toggle_favorite(request, article_id):
    """Adiciona/Remove favorito (AJAX)"""
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=401)
    
    article = get_object_or_404(Article, id=article_id)
    
    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        article=article
    )
    
    if not created:
        # Se já existe, remove
        favorite.delete()
        return JsonResponse({'status': 'removed', 'message': 'Removido dos favoritos'})
    else:
        return JsonResponse({'status': 'added', 'message': 'Adicionado aos favoritos'})


def fetch_news(request):
    """View administrativa para buscar notícias manualmente"""
    
    service = NewsAPIService()
    articles = service.fetch_culture_news(page_size=30)
    
    # Adiciona mensagem de sucesso
    if articles:
        messages.success(request, f'✅ {len(articles)} notícias foram buscadas e salvas com sucesso!')
    else:
        messages.warning(request, '⚠️ Nenhuma notícia foi encontrada. Verifique sua API key.')
    
    # Redireciona de volta pra home
    return redirect('news:home')