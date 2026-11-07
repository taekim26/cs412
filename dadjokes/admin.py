# File: dadjokes/admin.py
# Author: Tae Yeung Kim (kimty@bu.edu), 11/07/2026
# Description: admin for dadjokes application

from django.contrib import admin

# Register your models here.
from .models import Joke, Picture

admin.site.register(Joke)
admin.site.register(Picture)
