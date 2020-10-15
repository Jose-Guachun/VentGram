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
    def clean_objetive(self):
        objetive=self.cleaned_data['objetive'].title()
        SoloLetras(objetive, 'Objetivo')
        return objetive
        