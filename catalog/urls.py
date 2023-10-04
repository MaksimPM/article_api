from django.urls import path
from catalog.views import CatalogListView, ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDetailView, \
    ArticleDeleteView, BaseListView, toggle_activity

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('base/', BaseListView.as_view()),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
