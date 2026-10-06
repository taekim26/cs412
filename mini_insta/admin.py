# File: mini_insta/admin.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/06/2026
# Description: admin for mini_insta application

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
