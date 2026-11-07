# File: dadjokes/serializers.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/07/2026
# Description: serializers convert our django data models to a text-representation suitable to transmit over HTTP

from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''a serializer for the Joke model'''
    class Meta:
        model = Joke 
        fields = ['id' 'text', 'name', 'timestamp']

class PictureSerializer(serializers.ModelSerializer):
    '''a serializer for the Picture model'''
    class Meta:
        model = Picture 
        fields = ['id', 'image_url', 'name', 'timestamp']