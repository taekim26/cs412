# File: mini_insta/urls.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/01/2026
# Description: URL patterns for the mini_insta application

from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="show_profile"),
    path('post/<int:pk>', PostDetailView.as_view(), name="show_post"),
]