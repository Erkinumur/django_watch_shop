from django.urls import path

from .views import IndexView, WatchDetailView, WatchListView, FilterListView, SearchProductView, AddReview, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('detail/<int:pk>/', WatchDetailView.as_view(), name='watch_detail'),
    path('product_list/', WatchListView.as_view(), name='product_list'),
    path('product_list/filter/', FilterListView.as_view(), name='filter'),
    path('product_list/search/', SearchProductView.as_view(), name='search'),
    path('add_review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('about/', AboutView.as_view(), name='about'),
]