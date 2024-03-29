#Django
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core import validators
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#models
from users.models import Profile, User, Province, City
from VentGram.validators import SoloLetras, SoloNumeros, NumerosYLetras
from users.mail import send_email


class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=[
            "dni",
            "country",
            "province",
            "city",
            "gender", 
            "birth_date", 
            "biography", 
            "phone_number", 
            "education_level", 
            "work_area", 
            "home_address",
            "picture"]
    widgets = {
    'education_level': forms.Select(attrs={'class': 'form-control'}),
    'gender': forms.Select(attrs={'class': 'form-control'}),
    }
    def clean_work_area(self):
        work_area=self.cleaned_data['work_area'].title()
        SoloLetras(work_area, 'Medio en el que laboras')
        return  work_area


class SocialNetForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            "facebook",
            "twitter",
            "linkedin",
            "github", 
            ]

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username", "first_name", "last_name"]
    
    def clean_first_name(self):
        first_name=self.cleaned_data['first_name'].title()
        SoloLetras(first_name, 'Nombre')
        return first_name

    def clean_last_name(self):
        last_name=self.cleaned_data['last_name'].title()
        SoloLetras(last_name, 'Apellido')
        return last_name

    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].capitalize()
        NumerosYLetras(username)
        return username

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].lower()
        return username

class SignupForm(forms.ModelForm):
    password=forms.CharField(label=False, max_length=70, widget=forms.PasswordInput(),)
    password_confirmation=forms.CharField(label=False, max_length=70, widget=forms.PasswordInput(),)
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['password'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['password_confirmation'].required = True,

    class Meta:
        model=User
        fields=('email', 'username', 'first_name', 'last_name', 'code')

    def clean_first_name(self):
        first_name=self.cleaned_data['first_name'].title()
        SoloLetras(first_name, 'Nombre')
        return first_name

    def clean_last_name(self):
        last_name=self.cleaned_data['last_name'].title()
        SoloLetras(last_name, 'Apellido')
        return last_name

    def clean_email(self):
        #validacion del email
        email=self.cleaned_data['email'].lower()
        email_taken=User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('El email ingresado ya esta en uso. ')
        return email


    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].capitalize()
        username_taken=User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El usuario ingresado ya esta en uso.')
        if not username.isalnum():
            raise forms.ValidationError('En el campo Nombre de Usuario debe ingresar solo numeros y letras sin ningun espacio.')
        return username
        
    def clean(self):
        data=super().clean()
        try:
            password=data['password']
            password_confirmation=data['password_confirmation']
            if len(password)>7:
                if password.islower() or password.isupper() :
                    msg="La contraseña tiene que tener por lo menos 1 letra mayuscula y 1 minuscula"
                    self.add_error('password', msg)
                if password.isdigit() or  password.isalpha():
                    msg="La contraseña tiene que contener numeros, letras y simbolos especiales"
                    self.add_error('password', msg)
            else:
                msg="La contraseña tiene que tener como minimo 6 digitos"
                self.add_error('password', msg)

            if password != password_confirmation:
                msg="Contraseña no coincide"
                self.add_error('password_confirmation', msg)
            return data
        except:
            msg="La contraseña no tiene que estar conformada solo de espacios en blanco"
            self.add_error('password', msg)

        
        

    def save(self):
        #create user and profile
        data=self.cleaned_data
        data.pop('password_confirmation')
        
        user= User.objects.create_user(**data)
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        user.code=token
        user.save()
        send_email(user.email, token)
        profile=Profile(user=user)
        profile.save()
