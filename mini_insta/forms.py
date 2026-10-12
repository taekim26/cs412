# File: mini_insta/forms.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/11/2026
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
    '''a form to handle an update to a Post'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Profile 
        fields = ['display_name', 'profile_image_url', 'bio_text']
