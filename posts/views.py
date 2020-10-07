#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from users.models import Profile
from posts.models import Project, Category
#forms
from posts.forms import ProjectForm


def FilterProjectView(request):
    busqueda = request.GET.get("buscar")
    projects = Project.objects.all()
    if busqueda:
        projects = Project.objects.filter(
            Q(title__icontains = busqueda) |  
            Q(description__icontains = busqueda) 
        ).distinct()
    paginator=Paginator(projects, 6)
    page=request.GET.get('page')
    projects=paginator.get_page(page)
    return render(request, 'posts/list_project.html', {'projects':projects})

def ProjectFeedVie(request):
    busqueda = request.GET.get("buscar")
    projects = Project.objects.all()
    if busqueda:
        projects = Project.objects.filter(
            Q(title__icontains = busqueda) | 
            Q(description__icontains = busqueda) 
        ).distinct()
    paginator=Paginator(projects, 6)
    page=request.GET.get('page')
    projects=paginator.get_page(page)
    return render(request, 'posts/feed.html', {'projects':projects})

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
    paginate_by=6
    context_object_name='projects'
    
class CreatedProjectView(LoginRequiredMixin, CreateView):
    #Crear un nuevo post
    template_name='posts/new_project.html'
    form_class=ProjectForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all()
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
  
class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'



