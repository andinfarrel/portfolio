from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50,default='')
    title = models.CharField(max_length=50)
    text_snippet = models.CharField(max_length=20000)
    full_text = models.TextField(default="")
    pub_date = models.DateTimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def pubish(self):
        self.published_date = timezone.now()
        self.save()

class Project(models.Model):
    title = models.CharField(max_length=50,default='')
    cover_image = models.ImageField(upload_to='blog/static/images', height_field=None, width_field=None, max_length=None)
    text_snippet = models.CharField(max_length=20000)
    link = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
    
class Contact(models.Model):
    platform_name = models.CharField(default="", max_length=50)
    url = models.URLField(default="", max_length=200)
    image = models.ImageField(upload_to='blog/static/images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.platform_name

    def publish(self):
        self.save()