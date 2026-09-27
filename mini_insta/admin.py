# File: mini_insta/admin.py
# Author: Tae Yeung Kim (kimty@bu.edu), 09/26/2026
# Description: admin for mini_insta application

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)
