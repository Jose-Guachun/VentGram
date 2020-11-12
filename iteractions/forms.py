from django import forms
from iteractions.models import Comment

class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'cols':'120', 'rows':'10','class': 'form-control', ' placeholder':'Publicar un comentario',
	'type':'text','id':'id_body'}), required=True)

	class Meta:
		model = Comment
		fields = ('body',)