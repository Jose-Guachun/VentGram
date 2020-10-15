#user views
#Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import login, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, TemplateView, DetailView 
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.template import Context
from django.core.paginator import Paginator

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#Django decorators
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

#Models
from users.models import Profile, User, City, Province, Country
from posts.models import Project

#Forms
from users.forms import ProfileForm, SignupForm, LoginForm, UserForm
from django.contrib.auth.forms import AuthenticationForm


class UserDetailView(LoginRequiredMixin ,DetailView):
    #User detail view

    template_name='profile/profile.html'
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user=self.get_object()
        projects=Project.objects.filter(user=user).order_by('-created')
        projectsProfile=Project.objects.filter(user=user).order_by('-created')

        paginator=Paginator(projects, 2)
        page=self.request.GET.get('page')
        projects=paginator.get_page(page)

        context['projects']=projects
        context['projectsPro']=projectsProfile
        return context


class UpdateProfileView(FormView, LoginRequiredMixin, UpdateView):
    #update profile view
    template_name='profile/account_setting.html'
    form_class=ProfileForm
    def get_object(self):
        #return user profile
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        studies=('Primaria', 'Secundaria', 'Superior', 'Maestria', 'Doctorado')
        work=('Desarrollo', 'Marketing', 'Diseño', 'Negocios', 'Electronica')
        gender=('Masculino', 'Femenino', 'Otro')

        context['countrys']=Country.objects.all()
        context['studies'] = studies
        context['work'] = work
        context['gender']= gender
        return context
    
    def get_success_url(self):
        #Return to users profile.
        return reverse('users:setting')

def load_province(request):
    country=request.GET.get('country')
    provinces=Province.objects.filter(country=country).order_by('name_province')
    return render(request, 'profile/province_dropdown_list.html',{'provinces':provinces})

class UpdateUserView(FormView, LoginRequiredMixin, UpdateView):
    #update User view
    template_name='profile/account_setting.html'
    form_class=UserForm
    
    def get_object(self):
        #return user profile
        return self.request.user
    
    def get_success_url(self):
        #Return to users profile.
        return reverse('users:setting')

class LoginView(FormView):
    #login view
    template_name='users/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('posts:feed')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class SignupView(FormView):
    #Signup con classe base view
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        #save form data
        form.save()
        return super().form_valid(form)
        
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name='users/logget_auth.html'


def send_email(mail):
    context={'mail': mail}

    template=get_template('users/correo.html')
    content=template.render(context)

    email=EmailMultiAlternatives(
        'un correo de prueba',
        'hola ue hace',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def email_verified(request):
    if request.method== 'POST':
        mail = request.POST.get('mail')

        send_email(mail)

    return render(request, 'users/mail.html', {})