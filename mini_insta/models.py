# File: mini_insta/models.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/06/2026
# Description: data model for mini_insta application

from django.db import models
from django.urls import reverse

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
        return f'{self.username}'

    def get_all_posts(self):
        '''return a QuerySet of posts about this profile'''
        posts = Post.objects.filter(profile=self).order_by('timestamp')

        return posts

class Post(models.Model):
    '''Encapsulates the data of a mini_insta Post of the user'''
    # data attributes of the Post object
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.caption}'

    def get_all_photos(self):
        '''return a QuerySet of photos about this post'''
        photos = Photo.objects.filter(post=self).order_by('timestamp')

        return photos

    def get_absolute_url(self):
        '''return the URL to display one instance of this model'''

        return reverse('show_post', kwargs={'pk': self.pk})

class Photo(models.Model):
    '''Encapsulates the data of a mini_insta Photo of the Post'''
    # data attributes of the Photo object
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        if self.image_url:
            return f'Photo {self.pk} of {self.post} (url: {self.image_url})'
        else:
            return f'Photo {self.pk} of {self.post} (file: {self.image_file})'

    def get_image_url(self):
        '''return the URL to the image;
        URL either in the image_url attribute or image_file attribute as image_file.url'''
        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url
