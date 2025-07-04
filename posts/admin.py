# posts/admin.py
from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # Este campo preenche o 'slug' automaticamente a partir do 'name'
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista de posts
    list_display = ('title', 'author', 'category', 'status', 'publication_date')
    # Filtros que aparecerão na barra lateral direita
    list_filter = ('status', 'publication_date', 'category')
    # Campo de busca que procurará no título e conteúdo
    search_fields = ('title', 'content')
    # Preenche o 'slug' automaticamente a partir do 'title'
    prepopulated_fields = {'slug': ('title',)}
    # Ajuda a selecionar o autor de forma mais eficiente
    raw_id_fields = ('author',)
    # Adiciona uma navegação por datas
    date_hierarchy = 'publication_date'
    # Ordem padrão da lista
    ordering = ('status', 'publication_date')