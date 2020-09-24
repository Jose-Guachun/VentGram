#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView
from django.shortcuts import render


def TruncateText(request):
    cadena=request.POST.Profile('profile.biography')
    subcadena=cadena[:150]
    return subcadena

class ViewProjectView(TemplateView):
    template_name='posts/view_project.html'

class PostProjectView(TemplateView):
    template_name='posts/list_project.html'

# Create your views here.
class PostFeedView(LoginRequiredMixin, TemplateView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'

    
class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'



