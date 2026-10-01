# File: mini_insta/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/01/2026
# Description: class-based view for mini_insta application

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Photo

# Create your views here.
class ProfileListView(ListView):
    '''define a view class to show all mini_insta Profiles'''
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''display a single profile'''
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

class PostDetailView(DetailView):
    '''display a single post'''
    model = Post 
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

