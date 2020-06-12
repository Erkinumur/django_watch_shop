from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse

from .models import Watch, Group, Brand
from .forms import AuthUserForm


class FilterMixin:
    def get_categories(self):
        return Group.objects.all().order_by('name')

    def get_brands(self):
        return Brand.objects.all().order_by('name')

    def get_min_max_price(self):
        min_price = Watch.objects.order_by('price').first().price
        max_price = Watch.objects.order_by('-price').first().price
        return {'min': min_price, 'max': max_price}


class WatchCreateView(generic.CreateView):
    model = Watch
    fields = '__all__'
    template_name = 'catalog/watch_new.html'


class WatchUpdateView(generic.UpdateView):
    model = Watch
    fields = '__all__'
    template_name = 'catalog/watch_edit.html'


class WatchDeleteView(generic.DeleteView):
    model = Watch
    success_url = reverse_lazy('index_page')


class WatchListView(FilterMixin, generic.ListView):
    model = Watch
    template_name='catalog/product_list.html'

    paginate_by = 6


class WatchDetailView(generic.DetailView):
    model = Watch
    template_name = 'catalog/product_detail.html'


class IndexView(generic.ListView):
    model = Watch
    template_name = 'catalog/index.html'

    def get_queryset(self):
        return Watch.objects.all().order_by('-create_at')[:8]


class FilterListView(FilterMixin, generic.ListView):
    model = Watch
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        queryset = Watch.objects.filter(
            Q(group__in=self.request.GET.getlist('category')),
            Q(brand__in=self.request.GET.getlist('brand'))
        ).distinct()
        return queryset


class SearchProductView(FilterMixin, generic.ListView):
    model = Watch
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        return Watch.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context