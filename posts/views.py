#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView, CreateView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

#Model
from users.models import Profile
from posts.models import Project
#forms
from posts.forms import ProjectForm


class ProjectFeedView(LoginRequiredMixin, ListView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'
    model=Project
    ordering=('-created',)
    paginate_by=20
    context_object_name='posts'

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

class ViewProjectView(TemplateView):
    template_name='posts/view_project.html'

class PostProjectView(TemplateView):
    template_name='posts/list_project.html'

# Create your views here.
class PostFeedView(LoginRequiredMixin,  ListView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'
    model=Project
    ordering=('-created',)
    paginate_by=20
    context_object_name='projects'

    
class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'



