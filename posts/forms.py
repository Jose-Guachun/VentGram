#Django
from django import forms

#Models
from posts.models import Project
from VentGram.validators import SoloLetras


class ProjectForm(forms.ModelForm):
    
    STATUS_CHOICES=("Iniciado", "En Proceso", "Finalizado")
    class Meta:
        model=Project
        fields=[
            'user', 
            'profile',
            'category',
            'title',
            "label",
            'description', 
            'objetive',
            'image',
            'status',
            'typeProject',
            'website',
            'document',
            'collaborators',
            'views',
            ]
    def clean_title(self):
        title=self.cleaned_data['title'].capitalize()
        return title

    def clean_collaborators(self):
        collaborators=self.cleaned_data['collaborators'].title()
        SoloLetras(collaborators, 'Colaboradores')
        return collaborators

    def clean_objetive(self):
        objetive=self.cleaned_data['objetive'].capitalize() 
        return objetive
            
    widgets = {
        'category': forms.Select(attrs={'class': 'form-control'}),
        'typeProject': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
    }

