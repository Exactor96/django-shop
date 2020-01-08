from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('',views.search_index,name='search')
]