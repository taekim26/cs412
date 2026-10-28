# File: voter_analytics/urls.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/25/2026
# Description: URL patterns for the voter_analytics application

from django.urls import path
from . import views 
 
urlpatterns = [
	path(r'', views.VotersListView.as_view(), name='voters'),
    path(r'home', views.VotersListView.as_view(), name='home'),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name='voter'),
    path('graphs', views.GraphsListView.as_view(), name='graphs'),
]