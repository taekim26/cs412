# File: dadjokes/models.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/07/2026
# Description: data model for dadjokes application

from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Encapsulate the data for a joke'''
    text = models.TextField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.text}'

class Picture(models.Model):
    '''Encapsulate the data for picture or GIF'''
    image_url = models.URLField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.image_url}'
