from apps.common import utils

from django.conf import settings
from django.urls import reverse
from django.db import models
from apps.follow.models import Follow


AUTH_USER_MODEL = settings.AUTH_USER_MODEL


class Profile(models.Model):

	owner					= 	models.OneToOneField(to=AUTH_USER_MODEL,related_name='profile',on_delete=models.CASCADE)
	pic 					= 	models.ImageField(upload_to=utils.profile_dp,blank=True,null=True)
	full_name				=   models.CharField(max_length=250,blank=True,null=True)
	phone_number			= 	models.CharField(max_length=13,blank=True,null=True)
	bio 					= 	models.TextField(max_length=110,blank=True,null=True)
	gender					= 	models.CharField(max_length=6,blank=True,null=True)
	dob						=   models.DateField(blank=True,null=True)


	created 				=   models.DateTimeField(auto_now_add=True)
	update					=   models.DateTimeField(auto_now=True)

	class Meta:
		ordering 			= ('-created',)
		verbose_name 		= 'Profile'
		verbose_name_plural = 'Profiles'


	def __str__(self):
		return self.owner.username


	@property
	def user_followers(self):
		return Follow.get_people_following_user(self.owner)


	def get_absolute_url(self):
		return reverse('account:user-profile',args=[str(self.owner.username)])
	
	
	@property
	def pic_url(self):
		if self.pic:
			return self.pic.url
		return utils.default_avatar_url()


	

	


