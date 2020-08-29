from django.shortcuts import render, get_object_or_404
from .models import Post, Project, Contact
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    projects = Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    contacts = Contact.objects.all()
    return render(request, 'blog/base.html', {'posts':posts, 'projects':projects, 'contacts':contacts})

def blog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/blog_post.html', {'post':post})

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'blog/project_page.html', {'project':project})