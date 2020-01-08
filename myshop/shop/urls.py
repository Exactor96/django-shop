from django.conf.urls import url
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
app_name = 'shop'
urlpatterns = [
    path('<slug:category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<int:id>/<slug:slug>/', views.ProductDetail, name='ProductDetail'),
    path('', views.ProductList, name='ProductList'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)