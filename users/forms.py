#Django
from django import forms
from django.contrib.auth.forms import AuthenticationForm
#models
from users.models import Profile, User
from VentGram.validators import SoloLetras, SoloNumeros


class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=[
            "dni",
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
    'work_area': forms.Select(attrs={'class': 'form-control'}),
    'gender': forms.Select(attrs={'class': 'form-control'}),
    }

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email"]
    
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
        return email

    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].capitalize()
        if not username.isalnum():
            raise forms.ValidationError('En el campo Nombre de Usuario debe ingresar solo numeros y letras sin ningun espacio.')
        return username

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "password"]

class SignupForm(forms.ModelForm):
    password=forms.CharField(label=False, max_length=70, widget=forms.PasswordInput(),)
    password_confirmation=forms.CharField(label=False, max_length=70,  widget=forms.PasswordInput(),)
    
    class Meta:
        model=User
        fields=('email', 'username', 'first_name', 'last_name')

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

