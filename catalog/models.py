from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Описание')
    preview = models.ImageField(verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='Категория')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
