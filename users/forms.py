#Django
from django import forms

#models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    first_name=forms.CharField(label=False,min_length=2, max_length=50,)
    last_name=forms.CharField(label=False,min_length=2, max_length=50,)
    email=forms.CharField(label=False, min_length=6, max_length=70,widget=forms.EmailInput(),)
    username=forms.CharField(label=False, min_length=4, max_length=50,)
    password=forms.CharField(label=False, max_length=70, widget=forms.PasswordInput(),)
    password_confirmation=forms.CharField(label=False, max_length=70,  widget=forms.PasswordInput(),)
    
    

    def clean_email(self):
        #validacion del email
        email=self.cleaned_data['email'].lower()
        email_taken=User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('El email ingresado ya esta en uso. ')
        return email


    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].lower()
        username_taken=User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El usuario ingresado ya esta en uso.')
        return username
    
    def clean(self):
        data=super().clean()
        password=data['password']
        password_confirmation=data['password_confirmation']

        if password != password_confirmation:
            msg="Contraseña no coincide"
            self.add_error('password', msg)
        return data

    def save(self):
        #create user and profile
        data=self.cleaned_data
        data.pop('password_confirmation')

        user= User.objects.create_user(**data)
        profile=Profile(user=user)
        profile.save()
   