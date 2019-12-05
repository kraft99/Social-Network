from apps.common import utils

from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404

from apps.post.models import Post
from django.db import models



class Favorite(models.Model):

	user 		= models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='favorited_by')
	post 		= models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='favorites')

	create		= models.DateTimeField(auto_now_add=True)
	update		= models.DateTimeField(auto_now=True)



	class Meta:
		unique_together 	= (('user','post'),)
		verbose_name		= 'Favorite'
		verbose_name_plural = 'Favorites'


	def __str__(self):
		return "{0} added {1} to favorites".format(self.user.username,self.post.title)


	@property
	def readable_time(self):
		return utils.human_readable_time(self.created)