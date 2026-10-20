# File: mini_insta/models.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/19/2026
# Description: data model for mini_insta application

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a mini_insta Profile of the user'''
    # data attributes of the Profile object
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.username}'

    def get_all_posts(self):
        '''return a QuerySet of posts about this profile'''
        posts = Post.objects.filter(profile=self).order_by('timestamp')

        return posts

    def get_absolute_url(self):
        '''return the URL to display one instance of this model'''
        return reverse('show_profile', kwargs={'pk': self.pk})

    def get_followers(self):
        '''return a list of those Profiles who are followers of this profile'''
        follows = Follow.objects.filter(profile=self)
        # in list format
        followers = []
        for follow in follows:
            followers.append(follow.follower_profile)

        return followers

    def get_num_followers(self):
        '''return the count of followers'''
        return Follow.objects.filter(profile=self).count()

    def get_following(self):
        '''return a list of those Profiles followed by this profile'''
        follows = Follow.objects.filter(follower_profile=self)
        # in list format
        following = []
        for follow in follows:
            following.append(follow.profile)

        return following 

    def get_num_following(self):
        '''return the count of how many profiles are being followed'''
        return Follow.objects.filter(follower_profile=self).count()

    def get_num_posts(self):
        '''return the count of Posts made by this Profile'''
        return Post.objects.filter(profile=self).count()

    def get_post_feed(self):
        '''return a QuerySet of Posts made by the Profiles this Profile follows'''
        # list of publishers
        following = self.get_following()
        # filter Posts
        posts = Post.objects.filter(profile__in=following).order_by('-timestamp')

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

    def get_all_comments(self):
        '''return a QuerySet of comments of this Post'''
        return Comment.objects.filter(post=self).order_by('timestamp')

    def get_likes(self):
        '''return a QuerySet of likes of this Post'''
        return Like.objects.filter(post=self)

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

class Follow(models.Model):
    '''Encapsulates the idea of an edge connecting two nodes within the social network'''
    # data attributes of the Follow object
    # profile indicates which profile is being followed (publisher)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    # follower_profile indicates which profile is doing the following (subscriber)
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.follower_profile.display_name} follows {self.profile.display_name}'

class Comment(models.Model):
    '''Encapsulates the idea of one Profile providing a comment on a Post'''
    # data attributes of the Comment object
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.text} by {self.profile.username}'

class Like(models.Model):
    '''Encapsulates the idea of one Profile providing approval of a Post'''
    # data attributes of the Like object
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.profile.username} liked {self.post.caption}'
