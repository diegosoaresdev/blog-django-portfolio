from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True); slug = models.SlugField(max_length=100, unique=True, blank=True);
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self): return self.name
    class Meta: verbose_name = "Categoria"; verbose_name_plural = "Categorias"

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Rascunho'), ('published', 'Publicado')); title = models.CharField(max_length=200, verbose_name="Título"); slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="Deixe em branco para gerar automaticamente."); author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Autor"); category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name="Categoria"); content = models.TextField(verbose_name="Conteúdo"); publication_date = models.DateTimeField(default=timezone.now, verbose_name="Data de Publicação"); status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Status"); image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="Imagem de Destaque"); meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Descrição (SEO)"); meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Palavras-chave (SEO)")
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ('-publication_date',); verbose_name = "Post"; verbose_name_plural = "Posts"
# Create your models here.
