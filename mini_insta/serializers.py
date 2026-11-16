# File: mini_insta/serializers.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/15/2026
# Description: serializers convert our django data models to a text-representation suitable to transmit over HTTP

from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    '''a serializer for the Profile model'''
    class Meta:
        model = Profile 
        fields =  ['id', 'username', 'display_name', 'profile_image_url', 'bio_text', 'join_date']

class PostSerializer(serializers.ModelSerializer):
    '''a serializer for the Post model'''
    class Meta:
        model = Post 
        fields =  ['id', 'profile', 'timestamp', 'caption']

class PhotoSerializer(serializers.ModelSerializer):
    '''a serializer for the Photo model'''
    class Meta:
        model = Photo 
        fields =  ['id', 'post', 'timestamp', 'image_url', 'image_file']
