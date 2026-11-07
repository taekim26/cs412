# File: dadjokes/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/07/2026
# Description: class-based view for dadjokes application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse
from .models import Joke, Picture
from rest_framework import generics
from .serializers import *

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

# REST API views
class JokeListAPIView(generics.ListCreateAPIView):
    '''GET: list all jokes, POST: create a new joke'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveAPIView):
    '''GET: sinlge joke'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class RandomJokeAPIView(generics.RetrieveAPIView):
    '''GET: single random joke'''
    serializer_class = JokeSerializer

    def get_object(self):
        return random.choice(Joke.objects.all())

class PictureListAPIView(generics.ListAPIView):
    '''GET: list all pictures'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveAPIView):
    '''GET: single picture'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomPictureAPIView(generics.RetrieveAPIView):
    '''GET: single random picture'''
    serializer_class = PictureSerializer

    def get_object(self):
        return random.choice(Picture.objects.all())