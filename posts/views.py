#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView
from django.shortcuts import render


# Create your views here.
class PostFeedView(LoginRequiredMixin, TemplateView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'

