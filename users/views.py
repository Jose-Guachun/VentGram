# user views
# Django

from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import login, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.template import Context
from django.core.paginator import Paginator

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Django decorators
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


# Models
from users.models import Profile, User, City, Province, Country
from posts.models import Project

# Forms
from users.forms import ProfileForm, SignupForm, LoginForm, UserForm, SocialNetForm
from django.contrib.auth.forms import AuthenticationForm


class UserDetailView(LoginRequiredMixin, DetailView):
    # User detail view

    template_name = 'profile/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        projects = Project.objects.filter(user=user).order_by('-created')
        projectsProfile = Project.objects.filter(
            user=user).order_by('-created')

        paginator = Paginator(projects, 2)
        page = self.request.GET.get('page')
        projects = paginator.get_page(page)

        context['projects'] = projects
        context['projectsPro'] = projectsProfile
        return context


class UpdateProfileView(FormView, LoginRequiredMixin, UpdateView):
    # update profile view
    template_name = 'profile/update_profile.html'
    form_class = ProfileForm

    def get_object(self):
        # return user profile
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        studies = ('Primaria', 'Secundaria','Superior', 'Maestria', 'Doctorado')
        work = ('Desarrollo', 'Marketing', 'Diseño', 'Negocios', 'Electronica', 'Otro')
        gender = ('Masculino', 'Femenino', 'Otro')

        country=self.object.user.profile.country
        provinces = Province.objects.filter(country=country).order_by('name_province')

        province=self.object.user.profile.province
        citys = City.objects.filter(province=province).order_by('name_city')

        context['countrys'] = Country.objects.all()
        context['provinces'] = provinces
        context['citys'] = citys
        context['studies'] = studies
        context['work'] = work
        context['gender'] = gender
        return context

    def get_success_url(self):
        # Return to users profile.
        messages.success(
            self.request, 'Se modifico correctamente su perfil de usuario')
        return reverse('users:update_profile')

def load_province(request):
    country = request.GET.get('country')
    provinces = Province.objects.filter(
        country=country).order_by('name_province')
    return render(request, 'profile/province_dropdown_list.html', {'provinces': provinces})

def load_city(request):
    province = request.GET.get('province')
    citys = City.objects.filter(province=province).order_by('name_city')
    return render(request, 'profile/city_dropdown_list.html', {'citys': citys})


class UpdateSocialNet(LoginRequiredMixin, UpdateView):
    template_name = 'profile/social_net.html'
    form_class = SocialNetForm

    def get_object(self):
        # return user profile
        return self.request.user.profile

    def get_success_url(self):
        # Return to users profile.
        messages.success(
            self.request, 'Se agrego correctamente sus redes sociales')
        return reverse('users:social_net')


class UpdateUserView(FormView, LoginRequiredMixin, UpdateView):
    # update User view
    template_name = 'users/update_user.html'
    form_class = UserForm

    def get_object(self):
        # return user profile
        return self.request.user

    def get_success_url(self):
        # Return to users profile.
        messages.success(self.request, 'Se modifico correctamente su usuario')
        return reverse('users:update_user')


class UserChangePasswordView(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Se modifico correctamente su contraseña')
            return render(request, 'users/change_password.html')
        return render(request, 'users/change_password.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = 'Password'
        context['list_url'] = self.success_url
        return context

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('user:login')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # return user profile
        return self.request.user

    def post(self, request, *args, **kwargs):
        try:
            if request.method == 'POST':
                username = request.user.email
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    self.object.delete()
                    return redirect('users:login')
                else:
                    return render(request, 'users/delete_user.html', {'error': 'La contraseña ingresada no coicide' })
            return render(request, 'users/login.html')
        except Exception as e:
            messages.error(request, 'Ocurrio un erro no se puede eliminar cuenta')
        return render(request, 'users/login.html')


class LoginView(FormView):
    # login view
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
        if form.is_verified:
            login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return reverse_lazy('users:login')
        

class SignupView(FormView):
    # Signup con classe base view
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        # save form data
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            send_email(email)
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
