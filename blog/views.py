from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Post, Project, Contact, SkillsCategory, SkillItem, Experience
from .forms import SkillForm, ExperienceForm
# Create your views here.

def index(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    projects = Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    contacts = Contact.objects.all()
    skills_categories = SkillsCategory.objects.all()
    skills = SkillItem.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'blog/base.html', {'posts':posts, 'projects':projects, 'contacts':contacts, 'skills_categories':skills_categories,'skills':skills, 'experiences':experiences})

def blog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/blog_post.html', {'post':post})

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'blog/project_page.html', {'project':project})


class AddSkillView(TemplateView):

    template_name = 'blog/form.html'

    def get(self, request):
        form = SkillForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            return redirect('index')

        return render(request, self.template_name, {'form':form})

class AddExperienceView(TemplateView):

    template_name = 'blog/form.html'

    def get(self, request):
        form = ExperienceForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ExperienceForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            return redirect('index')

        return render(request, self.template_name, {'form':form})