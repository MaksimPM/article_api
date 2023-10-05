from django.urls import path
from catalog.views import CatalogListView, ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDetailView, \
    ArticleDeleteView, BaseListView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='/'),
    path('base/', BaseListView.as_view()),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('categories/', CategoryListView.as_view(), name='category'),
    path('create_categories/', CategoryCreateView.as_view(), name='create_category'),
    path('delete_categories/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('sort/<int:pk>/', CategoryDetailView.as_view(), name='sort_category')
]
