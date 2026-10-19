# File: mini_insta/urls.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/19/2026
# Description: URL patterns for the mini_insta application

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile', MyProfileDetailView.as_view(), name="my_profile"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="show_profile"),
    path('profile/create_post', CreatePostView.as_view(), name="create_post"),
    path('profile/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name="show_followers"),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name="show_following"),
    path('profile/feed', ShowFeedView.as_view(), name="show_feed"),
    path('profile/search', SearchView.as_view(), name="search"),
    path('profile/<int:pk>/follow', FollowProfileView.as_view(), name="follow"),
    path('profile/<int:pk>/delete_follow', DeleteFollowProfileView.as_view(), name="delete_follow"),
    path('post/<int:pk>', PostDetailView.as_view(), name="show_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/like', LikePostView.as_view(), name="like"),
    path('post/<int:pk>/delete_like', DeleteLikePostView.as_view(), name="delete_like"),
    # authorization-related URLs
    path('login/', auth_views.LoginView.as_view(template_name="mini_insta/login.html"), name="mini_insta_login"),
    path('logout_confirmation/', LogoutConfirmationView.as_view(), name="logout_confirmation"),
    path('logout/', auth_views.LogoutView.as_view(next_page="logout_confirmation"), name="mini_insta_logout"),
    path('create_profile/', CreateProfileView.as_view(), name="create_profile"),
]
