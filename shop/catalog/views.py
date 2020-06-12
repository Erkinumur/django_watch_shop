from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Watch


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


class WatchListView(generic.ListView):
    model = Watch
    template_name='catalog/product_list.html'


class WatchDetailView(generic.DetailView):
    model = Watch
    template_name = 'catalog/product_detail.html'


class IndexView(generic.ListView):
    model = Watch
    template_name = 'catalog/index.html'

    def get_queryset(self):
        return Watch.objects.all().order_by('-create_at')[:4]