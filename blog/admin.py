from django.contrib import admin

# Register your models here.
from .models import Post, Project, Contact

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Contact)