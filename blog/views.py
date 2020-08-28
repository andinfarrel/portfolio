from django.shortcuts import render, get_object_or_404
from .models import Post, Project
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    projects = Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/base.html', {'posts':posts, 'projects':projects})

def blog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/blog_post.html', {'post':post})