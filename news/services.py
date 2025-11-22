import requests
from django.conf import settings
from datetime import datetime
from .models import Article

class NewsAPIService:
    """Service para integração com NewsAPI"""
    
    def __init__(self):
        self.api_key = settings.NEWSAPI_KEY
        self.base_url = settings.NEWSAPI_BASE_URL
    
    def fetch_culture_news(self, language='en', country='us', page_size=20):
        """
        Busca notícias de cultura da NewsAPI (top-headlines)
        """
        url = f"{self.base_url}/top-headlines"
        
        params = {
            'apiKey': self.api_key,
            'category': 'entertainment',
            'language': language,
            'country': country,
            'pageSize': page_size
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data['status'] == 'ok':
                print(f"✅ API retornou {data.get('totalResults', 0)} notícias")
                return self._save_articles(data['articles'])
            else:
                print(f"❌ Erro da API: {data.get('message', 'Desconhecido')}")
                return []
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao buscar notícias: {e}")
            return []
    
    def fetch_news_by_theme(self, theme='cinema', language='en', page_size=30):
        """
        Busca notícias por tema cultural usando o endpoint /everything
        """
        # Mapeamento de temas para palavras-chave
        theme_keywords = {
            'cinema': 'cinema OR movie OR film OR hollywood OR streaming',
            'musica': 'music OR concert OR album OR artist OR band OR singer',
            'arte': 'art OR painting OR sculpture OR gallery OR museum OR exhibition',
            'literatura': 'book OR literature OR author OR novel OR poetry OR writer',
            'teatro': 'theater OR theatre OR play OR musical OR broadway OR performance',
            'games': 'gaming OR videogame OR esports OR game OR playstation OR xbox OR nintendo',
            'tv': 'television OR tv show OR series OR netflix OR streaming OR episode',
            'cultura': 'culture OR entertainment OR arts OR cultural',
        }
        
        keywords = theme_keywords.get(theme, theme_keywords['cultura'])
        
        url = f"{self.base_url}/everything"
        
        params = {
            'apiKey': self.api_key,
            'q': keywords,
            'language': language,
            'pageSize': page_size,
            'sortBy': 'publishedAt'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data['status'] == 'ok':
                print(f"✅ API retornou {data.get('totalResults', 0)} notícias sobre {theme}")
                return self._save_articles_with_theme(data['articles'], theme)
            else:
                print(f"❌ Erro da API: {data.get('message', 'Desconhecido')}")
                return []
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao buscar notícias: {e}")
            return []
    
    def _save_articles(self, articles_data):
        """
        Salva artigos no banco de dados
        """
        saved_articles = []
        
        for article_data in articles_data:
            # Pula artigos sem URL (inválidos)
            if not article_data.get('url'):
                continue
            
            # Converte published_at para datetime
            published_at = article_data.get('publishedAt')
            if published_at:
                published_at = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            
            # Cria ou atualiza o artigo
            article, created = Article.objects.update_or_create(
                url=article_data['url'],
                defaults={
                    'source_id': article_data['source'].get('id'),
                    'source_name': article_data['source'].get('name', 'Desconhecido'),
                    'author': article_data.get('author'),
                    'title': article_data.get('title', 'Sem título'),
                    'description': article_data.get('description'),
                    'url_to_image': article_data.get('urlToImage'),
                    'published_at': published_at,
                    'content': article_data.get('content'),
                    'category': 'culture'
                }
            )
            
            saved_articles.append(article)
        
        return saved_articles
    
    def _save_articles_with_theme(self, articles_data, theme):
        """
        Salva artigos no banco de dados com tema específico
        """
        saved_articles = []
        
        for article_data in articles_data:
            # Pula artigos sem URL (inválidos)
            if not article_data.get('url'):
                continue
            
            # Converte published_at para datetime
            published_at = article_data.get('publishedAt')
            if published_at:
                published_at = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            
            # Cria ou atualiza o artigo
            article, created = Article.objects.update_or_create(
                url=article_data['url'],
                defaults={
                    'source_id': article_data['source'].get('id'),
                    'source_name': article_data['source'].get('name', 'Desconhecido'),
                    'author': article_data.get('author'),
                    'title': article_data.get('title', 'Sem título'),
                    'description': article_data.get('description'),
                    'url_to_image': article_data.get('urlToImage'),
                    'published_at': published_at,
                    'content': article_data.get('content'),
                    'category': theme
                }
            )
            
            saved_articles.append(article)
        
        return saved_articles
    
    def search_news(self, query, language='en', page_size=20):
        """
        Busca notícias por palavra-chave
        """
        url = f"{self.base_url}/everything"
        
        params = {
            'apiKey': self.api_key,
            'q': query,
            'language': language,
            'pageSize': page_size,
            'sortBy': 'publishedAt'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data['status'] == 'ok':
                return self._save_articles(data['articles'])
            else:
                return []
                
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar notícias: {e}")
            return []