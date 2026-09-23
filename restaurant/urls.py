# File: restaurant/urls.py
# Author: Tae Yeung Kim (kimty@bu.edu), 09/23/2026
# Description: URL patterns for the restaurant app

from django.urls import path
from django.conf import settings
from . import views

# URL patterns for this app
urlpatterns = [
    path(r'main', views.main, name='main'),
    path(r'order', views.order, name='order'),
    path(r'confirmation', views.confirmation, name='confirmation'),
]