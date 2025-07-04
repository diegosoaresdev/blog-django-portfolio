# config/urls.py
from django.contrib import admin
from django.urls import path, include  # Note que estamos importando 'include'
from django.conf import settings         # Importamos as configurações
from django.conf.urls.static import static # E a função para arquivos estáticos/mídia

urlpatterns = [
    # A URL do painel de administração, que mantemos
    path('admin/', admin.site.urls),

    # Esta é a linha mais importante:
    # Ela diz ao Django para incluir o arquivo de URLs do nosso app 'posts'
    path('', include('posts.urls')),
]

# Este bloco é um truque para o modo de desenvolvimento.
# Ele permite que o servidor do Django encontre e mostre as imagens
# que você faz upload (arquivos de mídia).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)