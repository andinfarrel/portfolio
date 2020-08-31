from django.contrib import admin

# Register your models here.
from .models import Post, Project, Contact, SkillsCategory, SkillItem, Experience

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Contact)

admin.site.register(SkillsCategory)
admin.site.register(SkillItem)
admin.site.register(Experience)