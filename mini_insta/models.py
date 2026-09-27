# File: mini_insta/models.py
# Author: Tae Yeung Kim (kimty@bu.edu), 09/26/2026
# Description: data model for mini_insta application

from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a mini_insta Profile of the user'''
    # data attributes of the Profile object
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'"{self.username}"\'s profile info: {self.display_name}, {self.join_date}'

