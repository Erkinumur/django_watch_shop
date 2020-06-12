"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



from catalog.views import WatchCreateView, WatchUpdateView, WatchDeleteView, WatchListView, WatchDetailView
from catalog.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>/', WatchDetailView.as_view(), name='watch_detail'),
    path('', IndexView.as_view(), name='index_page'),
    path('product_list/', WatchListView.as_view(), name='product_list'),
    path('watch_new/', WatchCreateView.as_view(), name='watch_new'),
    path('edit/<int:pk>/', WatchUpdateView.as_view(), name='watch_edit'),
    path('delete/<int:pk>/', WatchDeleteView.as_view(), name='watch_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

