# File: dadjokes/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/07/2026
# Description: class-based view for dadjokes application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse
from .models import Joke, Picture

import random

# Create your views here.
class RandomView(TemplateView):
    '''show one random joke and one random picture'''
    template_name = 'dadjokes/random.html'

    def get_context_data(self, **kwargs):
        '''return the dictionary of context variables for use in the template'''
        context = super().get_context_data(**kwargs)
        context['joke'] = random.choice(Joke.objects.all())
        context['picture'] = random.choice(Picture.objects.all())

        return context 

class JokeListView(ListView):
    '''show all jokes'''
    model = Joke
    template_name = 'dadjokes/jokes.html'
    context_object_name = 'jokes'

class JokeDetailView(DetailView):
    '''show single joke'''
    model = Joke 
    template_name = 'dadjokes/joke.html'
    context_object_name = 'joke'

class PictureListView(ListView):
    '''show all pictures'''
    model = Picture 
    template_name = 'dadjokes/pictures.html'
    context_object_name = 'pictures'

class PictureDetailView(DetailView):
    '''show single picture'''
    model = Picture 
    template_name = 'dadjokes/picture.html'
    context_object_name = 'picture'