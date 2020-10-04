#Django
from django import forms

#Models
from posts.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        fields=[
            'user', 
            'profile',
            'title',
            'description', 
            'objetive',
            'image',
            'status',
            'website',
            'document',
            'collaborators',]
        