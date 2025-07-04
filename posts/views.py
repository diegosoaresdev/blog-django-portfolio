# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category # Importamos nossos "ingredientes"

# View para a página inicial (lista de posts)
def post_list(request):
    # 1. Busca no banco de dados todos os Posts com status 'published'
    # 2. .select_related() é um truque de performance para buscar os dados do autor e da categoria de uma vez só
    posts = Post.objects.filter(status='published').select_related('author', 'category')
    categories = Category.objects.all()

    # 3. Cria um "pacote" de dados para enviar ao template
    context = {
        'posts': posts,
        'categories': categories
    }

    # 4. Renderiza o template HTML, passando o "pacote" de dados
    return render(request, 'posts/post_list.html', context)

# View para a página de um único post
def post_detail(request, slug):
    # 1. Tenta encontrar um Post com o 'slug' vindo da URL. Se não achar, retorna um erro 404 (Página não encontrada).
    post = get_object_or_404(Post, slug=slug, status='published')
    categories = Category.objects.all()

    # 2. Cria o "pacote" de dados com o post encontrado
    context = {
        'post': post,
        'categories': categories
    }

    # 3. Renderiza o template de detalhe, passando os dados do post
    return render(request, 'posts/post_detail.html', context)

# View para a página de uma categoria
def category_posts(request, slug):
    # 1. Encontra a categoria pelo 'slug' da URL
    category = get_object_or_404(Category, slug=slug)
    # 2. Filtra todos os posts que pertencem a essa categoria
    posts = Post.objects.filter(category=category, status='published').select_related('author')
    categories = Category.objects.all()

    # 3. Cria o "pacote" de dados
    context = {
        'category': category,
        'posts': posts,
        'categories': categories
    }
    # 4. Reutiliza o mesmo template da lista de posts para mostrar o resultado
    return render(request, 'posts/post_list.html', context)
