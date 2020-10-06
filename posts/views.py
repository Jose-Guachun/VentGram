#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

#Model
from users.models import Profile
from posts.models import Project
#forms
from posts.forms import ProjectForm


class ProjectDetailView(LoginRequiredMixin, DetailView):
    #retornar detalle de post
    template_name='posts/detail_project.html'
    queryset=Project.objects.all()
    context_object_name='project'

class ProjectFeedView(LoginRequiredMixin, ListView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'
    model=Project
    ordering=('-created',)
    paginate_by=20
    context_object_name='projects'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        project=Project.objects.all()[5:6]
        context['description']=project[:20] 
        return context


class CreatedProjectView(LoginRequiredMixin, CreateView):
    #Crear un nuevo post
    template_name='posts/new_project.html'
    form_class=ProjectForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context


class PostProjectView(TemplateView):
    template_name='posts/list_project.html'

# Create your views here.


    
class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'



