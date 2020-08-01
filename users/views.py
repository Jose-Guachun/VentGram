#user views
#Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView

#Models


#Forms
from users.forms import SignupForm



class LoginView(auth_views.LoginView):
    #login view
    template_name='users/login.html'

class SignupView(FormView):
    #Signup con classe base view
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        #save form data
        form.save()
        return super().form_valid(form)