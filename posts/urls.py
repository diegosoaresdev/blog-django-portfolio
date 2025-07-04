# posts/urls.py
from django.urls import path
from . import views # Importa nosso arquivo de views

urlpatterns = [
    # URL da página inicial (ex: meusite.com/)
    path('', views.post_list, name='post_list'),

    # URL para um post específico (ex: meusite.com/post/meu-primeiro-post/)
    # <slug:slug> é uma variável que captura o texto da URL
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

    # URL para uma categoria específica (ex: meusite.com/categoria/programacao/)
    path('categoria/<slug:slug>/', views.category_posts, name='category_posts'),
]