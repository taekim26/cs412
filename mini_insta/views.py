# File: mini_insta/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/19/2026
# Description: class-based view for mini_insta application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin 

# subclass of LoginRequiredMixin
class MiniInstaLoginRequiredMixin(LoginRequiredMixin):
    '''subclass of LoginRequiredMixin for mini_insta views for logged in user'''
    def get_login_url(self):
        '''return the URL for the login page'''
        return reverse('mini_insta_login')

    def get_logged_in_profile(self):
        '''return the Profile of the logged-in user'''
        return Profile.objects.filter(user=self.request.user).first()

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

class MyProfileDetailView(MiniInstaLoginRequiredMixin, DetailView):
    '''display the logged-in user's profile'''
    model = Profile 
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        '''return the Profile of the logged-in user'''
        return self.get_logged_in_profile()

class PostDetailView(DetailView):
    '''display a single post'''
    model = Post 
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
 
class CreatePostView(MiniInstaLoginRequiredMixin, CreateView):
    '''a view to handle creation of a new Post on a Profile'''
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"
 
    def get_context_data(self):
        '''return the dictionary of context variables for use in the template'''
        context = super().get_context_data()
        context['profile'] = self.get_logged_in_profile()

        return context

    def form_valid(self, form):
        '''handles the form submission and saves the new object to the Django database;
            attach the Profile to the Post object before saving it to the database.'''
        form.instance.profile = self.get_logged_in_profile()
        response = super().form_valid(form)

        # create the Photo for the saved Post
        # image_url = self.request.POST['image_url']
        files = self.request.FILES.getlist('files')
        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return response

class UpdateProfileView(MiniInstaLoginRequiredMixin, UpdateView):
    '''view class to handle update of a logged-in user's profile'''
    model = Profile 
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_object(self):
        '''return the Profile of the logged-in user'''
        return self.get_logged_in_profile()

class DeletePostView(MiniInstaLoginRequiredMixin, DeleteView):
    '''view class to delete a post on a Profile'''
    model = Post 
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self, **kwargs):
        '''return the dictionary of context variables for use in the template'''
        context = super().get_context_data(**kwargs)
        # reference to the Post to be deleted
        post = self.object 
        # Profile of the user who made the Post
        profile = post.profile # profile is the FK that refers to Profile object
        # add this post and profile into the context dict
        context['post'] = post 
        context['profile'] = profile

        return context 

    def get_success_url(self):
        '''provide a URL to redirect to after successfully deleting a post'''
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

class UpdatePostView(MiniInstaLoginRequiredMixin, UpdateView):
    '''view class to handle update of a post based on its PK'''
    model = Post
    form_class = UpdatePostForm 
    template_name = "mini_insta/update_post_form.html"

class ShowFollowersDetailVeiw(DetailView):
    '''display followers information'''
    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    '''display following information'''
    model = Profile 
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

class ShowFeedView(MiniInstaLoginRequiredMixin, DetailView):
    '''display post feed for a logged-in user'''
    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = "profile"

    def get_object(self):
        '''return the Profile of the logged-in user'''
        return self.get_logged_in_profile()

class SearchView(MiniInstaLoginRequiredMixin, ListView):
    '''search feature to search user Profiles and Posts based on a text input'''
    template_name = "mini_insta/search_results.html"
    context_object_name = "post"

    def dispatch(self, request, *args, **kwargs):
        '''require login and return search.html template if the query is absent;
            return the superclass version of dispatch otherwise'''
        if not request.user.is_authenticated or 'query' in self.request.GET:
            return super().dispatch(request, *args, **kwargs)
        else:
            profile = self.get_logged_in_profile()
            context = {"profile": profile}

            return render(request, 'mini_insta/search.html', context)

    def get_queryset(self):
        '''return the Posts that contain the query'''
        # this reads the search text out of the URL and puts in a variable called query
        # the key 'query' comes from the name="query" attribute on the form's input in search.html
        query = self.request.GET.get('query', '')

        # used __icontains to make search NOT case sensitive
        return Post.objects.filter(caption__icontains=query).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        '''return the dictionary of context variables for use in the template'''
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('query', '')
        context['query'] = query
        context['profile'] = self.get_logged_in_profile()
        context['posts'] = self.get_queryset()

        profiles_username = Profile.objects.filter(username__icontains=query)
        profiles_display_name = Profile.objects.filter(display_name__icontains=query)
        profiles_bio_text = Profile.objects.filter(bio_text__icontains=query)

        profiles = []
        for match in profiles_username:
            if match not in profiles:
                profiles.append(match)
        for match in profiles_display_name:
            if match not in profiles:
                profiles.append(match)
        for match in profiles_bio_text:
            if match not in profiles:
                profiles.append(match)

        context['profiles'] = profiles

        return context

class LogoutConfirmationView(TemplateView):
    '''display a logout confirmation page'''
    template_name = "mini_insta/logged_out.html"
