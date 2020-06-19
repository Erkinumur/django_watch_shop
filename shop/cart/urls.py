from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('update/', views.cart_update, name='cart_update'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order_create/', views.order_create, name='order_create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
]