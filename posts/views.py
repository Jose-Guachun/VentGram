#Django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView
from django.shortcuts import render

#Model
from users.models import Profile

        


class ViewProjectView(TemplateView):
    template_name='posts/view_project.html'

class PostProjectView(TemplateView):
    template_name='posts/list_project.html'

# Create your views here.
class PostFeedView(LoginRequiredMixin, TemplateView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'

    def TruncateText(self):
        profile=self.request.user.profile
        cadena=profile.objects.POST['biography']
        biography=cadena[:20]
        return biography
    
class PostHomeView(TemplateView):
    #retornar todas las publicaciones
    template_name='home.html'



