from django.shortcuts import render
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from catalog.models import Article, Category


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ('category_name',)
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.save()

        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category')


class BaseListView(ListView):
    model = Article
    template_name = "catalog/base.html"


class CatalogListView(ListView):
    model = Article
    template_name = "catalog/article_list.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'category',)
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
    fields = ('title', 'content', 'category',)

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


def sort_articles(request, **kwargs):
    category_pk = kwargs.get('pk')
    queryset = Article.objects.filter(category=category_pk)
    context = {'queryset': queryset, 'category_pk': category_pk}
    return render(request, 'catalog/category_sort.html', context)

