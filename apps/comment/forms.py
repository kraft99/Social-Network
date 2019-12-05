from django import forms
from .models import Comment



class CommentCreateForm(forms.ModelForm):
	comment = forms.CharField(label="",widget=forms.TextInput())
	class Meta:
		model  = Comment
		fields = ('content',)