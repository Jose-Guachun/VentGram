#Django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

#models
from iteractions.models import Likes, Comment
from users.models import Profile, User
from posts.models import Project, Category, Status

#python
import time
#forms
from posts.forms import ProjectForm
from iteractions.forms import CommentForm


@login_required
def FilterProjectView(request):
    busqueda = request.POST.get("buscar")
    filtroCa=request.POST.get("filtroCategoria")
    filtroEs=request.POST.get("filtroEstado")
    projects = Project.objects.all()
    categorys = Category.objects.all()
    status = Status.objects.all()
    context=()
    if busqueda:
        projects = Project.objects.filter(
            Q(title__icontains = busqueda) |  
            Q(description__icontains = busqueda) 
        ).distinct()
    elif filtroCa:
        projects = Project.objects.filter(category=filtroCa)
        context=('Proyectos de ')
    elif filtroEs:
        context=('Proyectos con estado ')
        projects = Project.objects.filter(status=filtroEs)

    paginator=Paginator(projects, 6)
    page=request.GET.get('page')
    projects=paginator.get_page(page)
    return render(request, 'posts/list_project.html', {'projects':projects, 'categorys':categorys, 'statuss':status, 'context':context})

@login_required
def ProjectFeedView(request,**kwargs):
    busqueda = request.POST.get("buscar")
    projects = Project.objects.all()
    if busqueda:
        projects = Project.objects.filter(
            Q(title__icontains = busqueda) | 
            Q(description__icontains = busqueda) 
        ).distinct()

    paginator=Paginator(projects, 9)
    page=request.GET.get('page')
    projects=paginator.get_page(page)
    return render(request, 'posts/feed.html', {'projects':projects})

@login_required
def ProjectDetailView(request, url, project_id):
    project= get_object_or_404(Project, url=url)
    user= request.user
    profile= Profile.objects.get(user=user)
    favorited= False

    
    if project_id != 0:
        projects = Project.objects.get(url=url)
        if projects.user != user:
            views=projects.views+1
            Project.objects.filter(url=url).update(views=views)

    #like
    
    is_like= Likes.objects.filter(user=user, post=project).exists()

    #comment
    comments = Comment.objects.filter(post=project).order_by('-date')
    counts=Comment.objects.filter(post=project).count()

    if request.user.is_authenticated:
        profile= Profile.objects.get(user=user)

        if profile.favorites.filter(url=url).exists():
            favorited=True

	#Comments Form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = project
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('posts:detail_project', args=[url, 0]))	
    else:
        form = CommentForm()
    
    template = loader.get_template('posts/detail_project.html')
    context = {
        'project':project,
		'favorited':favorited,
		'profile':profile,
        'form':form,
        'comments':comments,
        'likes':is_like,
        'counts':counts,
    }
    return HttpResponse(template.render(context, request))

class CreatedProjectView(LoginRequiredMixin, CreateView):
    #Crear un nuevo post
    template_name='posts/create_update_project.html'
    form_class=ProjectForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
  
class UpdateProjectView(LoginRequiredMixin, UpdateView):
    #Crear un nuevo post
    template_name='posts/create_update_project.html'
    model=Project
    form_class=ProjectForm
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
        
    def get_success_url(self):
        #Return to users profile.
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model=Project
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_success_url(self):
        #Return to users profile.
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})

class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'