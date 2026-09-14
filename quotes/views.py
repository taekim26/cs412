# file: quotes/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

# hard-coded quotes from Charles Darwin
quotes = [
    "A man who dares to waste one hour of time has not discovered the value of life.",
    "Ignorance more frequently begets confidence than does knowledge.",
    "The love for all living creatures is the most noble attribute of man.",
]

# images of Charles Darwin
images = [
    "https://upload.wikimedia.org/wikipedia/commons/3/36/Charles_Darwin_photograph_by_Ernest_Edwards%2C_circa_1866.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
    "https://upload.wikimedia.org/wikipedia/commons/d/dd/Charles_Darwin_photograph_by_Ernest_Edwards%2C_1867.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
    "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3c/Charles_Darwin_01.jpg/1280px-Charles_Darwin_01.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
]

def quote(request):
    '''Selects one quote and one image, then delegate work to quote.html'''
    template_name = 'quotes/quote.html'
    context = {
        "quote": random.choice(quotes),
        "image": random.choice(images),
    }

    return render(request, template_name, context)

def show_all(request):
    '''Shows all quotes and images, then delegate work to show_all.html'''
    template_name = 'quotes/show_all.html'
    context = {
        "quotes": quotes,
        "images": images, 
    }

    return render(request, template_name, context)

def about(request):
    '''Information about the person, then delegate work to about.html'''
    template_name = 'quotes/about.html'

    return render(request, template_name)