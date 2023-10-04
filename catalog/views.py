from django.shortcuts import get_object_or_404, redirect
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from catalog.models import Article


class BaseListView(ListView):
    model = Article
    template_name = "catalog/base.html"


class CatalogListView(ListView):
    model = Article
    template_name = "catalog/article_list.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog')


def toggle_activity(pk):
    article_item = get_object_or_404(Article, pk=pk)
    article_item.is_published = False if article_item.is_published else True
    article_item.save()
    return redirect(reverse('catalog'))
