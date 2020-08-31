from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import AddSkillView, AddExperienceView

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<int:post_id>/', views.blog, name="blogpost"),
    path('project/<int:project_id>/', views.project, name="projectpage"),
    path('form/skill/', AddSkillView.as_view(), name="form_skill"),
    path('form/experience/', AddExperienceView.as_view(), name="form_exp"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
