# File: mini_insta/forms.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/19/2026
# Description: define the forms that we use for create/update/delete operations

from django import forms
from .models import *
 
class CreatePostForm(forms.ModelForm):
    '''a form to add a Post to the database'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Post 
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''a form to handle an update to a Profile'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Profile 
        fields = ['display_name', 'profile_image_url', 'bio_text']

class UpdatePostForm(forms.ModelForm):
    '''a form to handle an update to a Post'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Post 
        fields = ['caption']

class CreateProfileForm(forms.ModelForm):
    '''a form to add a new Profile to the database'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']

