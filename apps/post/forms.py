from django import form
from .models import Post



class PostCreateForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields	= ('title','content','photo',)