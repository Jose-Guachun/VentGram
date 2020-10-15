#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from users.models import Profile, User
from posts.models import Project, Category
#forms
from posts.forms import ProjectForm



@login_required
def FilterProjectView(request):
    busqueda = request.POST.get("buscar")
    filtro=request.POST.get("filtro")
    projects = Project.objects.all()
    categorys = Category.objects.all()
    if busqueda:
        projects = Project.objects.filter(
            Q(title__icontains = busqueda) |  
            Q(description__icontains = busqueda) 
        ).distinct()
    elif filtro:
        projects = Project.objects.filter(category=filtro)

    paginator=Paginator(projects, 4)
    page=request.GET.get('page')
    projects=paginator.get_page(page)
    return render(request, 'posts/list_project.html', {'projects':projects, 'categorys':categorys})

@login_required
def ProjectFeedView(request):
    busqueda = request.POST.get("buscar")
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
    
class CreatedProjectView(LoginRequiredMixin, CreateView):
    #Crear un nuevo post
    template_name='posts/create_update_project.html'
    form_class=ProjectForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all()
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
  
class UpdateProjectView(LoginRequiredMixin, UpdateView):
    #Crear un nuevo post
    template_name='posts/create_update_project.html'
    model=Project
    form_class=ProjectForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all()
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
        
    def get_success_url(self):
        #Return to users profile.
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model=Project

    def get_success_url(self):
        #Return to users profile.
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})

class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'