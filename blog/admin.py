from django.contrib import admin

# Register your models here.
from .models import Post, Project

admin.site.register(Post)
admin.site.register(Project)