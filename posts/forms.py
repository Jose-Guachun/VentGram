#Django
from django import forms

#Models
from posts.models import Project
from VentGram.validators import SoloLetras


class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        fields=[
            'user', 
            'profile',
            'category',
            'title',
            'description', 
            'objetive',
            'image',
            'status',
            'website',
            'document',
            'collaborators',]

    widgets = {
        'title': forms.TextInput(attrs={'placeholder':'Hola que hace '}),
        'category': forms.Select(attrs={'class': 'form-control', 'placeholder':'Seleccione una categoria'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'document': forms.FileInput(attrs={'class':'py-2', 'id':'id_document'},),
        'image': forms.FileInput(attrs={'class':'py-2', 'id':'file'},),
    }
        