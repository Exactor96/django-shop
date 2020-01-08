from django.conf.urls import url
from django.urls import path

from .views import CuponApply
app_name = 'cupons'
urlpatterns = [
    path('apply/', CuponApply, name='apply')
]