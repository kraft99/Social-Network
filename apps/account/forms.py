from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Profile
# crispy
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from crispy_forms.helper import FormHelper

from django import forms



class LoginForm(forms.Form):
	password 	= forms.CharField(label="password",widget=forms.TextInput(attrs={'placeholder':'*************'}))

	class Meta:
		model 	= get_user_model()
		fields  = ('username','password',)


class RegisterForm(forms.ModelForm):

	F = 'Female'
	M = 'Male'
	O = 'Other'

	GENDER = (
		(F,'Female'),
		(M,'Male'),
		(O,'Other'),
	)

	
	phone_number	= forms.CharField(max_length=250,required=True,label='Phone Number',widget=forms.TextInput(attrs={'placeholder':'phone number'}))
	username     	= forms.CharField(label="Username",required=True,widget=forms.TextInput(attrs={'placeholder':'Your Username'}))
	full_name		= forms.CharField(label="Full Name",required=True,widget=forms.TextInput(attrs={'placeholder':'Your Fullname'}))
	gender 			= forms.ChoiceField(label='Gender',choices=GENDER,required=True)
	password1		= forms.CharField(max_length=250,label='Password',widget=forms.PasswordInput(attrs={'placeholder':'**********'}))
	password2		= forms.CharField(max_length=250,label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'**********'}))

	class Meta:
		model = get_user_model()
		fields = ('phone_number','username','full_name','gender','password1','password2',)




class ProfileEditForm(forms.ModelForm):
	F = 'Female'
	M = 'Male'
	O = 'Other'

	GENDER = (
	(F,'Female'),
	(M,'Male'),
	(O,'Other'),
	)
	
	phone_number	= forms.CharField(max_length=250,required=True,label='Phone Number',widget=forms.TextInput(attrs={'placeholder':'phone number'}))
	full_name		= forms.CharField(label="Full Name",required=True,widget=forms.TextInput(attrs={'placeholder':'Your Fullname'}))
	gender 			= forms.ChoiceField(label='Gender',choices=GENDER,required=True)
	dob				= forms.DateField(label="Date of Birth",required=True)
	pic 	= forms.FileField(label="Picture",help_text='maximum file upload is 5KB, allowed image extensions;jpg or jpeg,png',required = False,widget=forms.FileInput(attrs={'accept':'image/*'}))

	class Meta:
		model 	= Profile
		fields 	= ('phone_number','full_name','bio','pic','gender','dob',)