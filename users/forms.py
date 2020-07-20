#Django
from django import forms

#models
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username=forms.CharField(
        label=False, min_length=4, max_length=50, 
        widget = forms.TextInput(
            attrs={
            'placeholder':'Usuario',
            'class': 'form-control',
            'required': True})
            )


    password=forms.CharField(
        label=False, max_length=70, 
        widget=forms.PasswordInput(
            attrs={
            'placeholder':'Contraseña',
            'class': 'form-control',
            'required': True})
            )


    password_confirmation=forms.CharField(
        label=False, max_length=70, 
        widget=forms.PasswordInput(
            attrs={
            'placeholder':'Confirmar Contraseña',
            'class': 'form-control',
            'required': True})
            )


    first_name=forms.CharField(
        label=False,min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
            'placeholder':'Nombre',
            'class': 'form-control',
            'required': True
            })
            )


    last_name=forms.CharField(
        label=False,min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
            'placeholder':'Apellido',
            'class': 'form-control',
            'required': True
            })
            )


    email=forms.CharField(
        label=False, min_length=6, max_length=70,
        widget=forms.EmailInput(
            attrs={
            'placeholder':'Email',
            'class': 'form-control',
            'required': True
            })
        )

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
            raise forms.ValidationError('contraseña no coincide')
        return data

   