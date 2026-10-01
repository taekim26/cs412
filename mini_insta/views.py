# File: mini_insta/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/01/2026
# Description: class-based view for mini_insta application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Profile, Post, Photo
from .forms import CreatePostForm

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

class CreatePostView(CreateView):
    '''a view to handle creation of a new Post on a Profile'''
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        '''return the dictionary of context variables for use in the template'''
        
        context = super().get_context_data()
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile

        return context

    def form_valid(self, form):
        '''handles the form submission and saves the new object to the Django database;
            attach the Profile to the Post object before saving it to the database.'''
        
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        response = super().form_valid(form)

        # create the Photo for the saved Post
        # image_url = self.request.POST['image_url']
        files = self.request.FILES.getlist('files')

        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return response
