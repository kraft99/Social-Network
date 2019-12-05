from apps.common import utils

from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404

from apps.post.models import Post
from django.db import models


class Comment(models.Model):

	user 		= models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment_by')
	post 		= models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='comments')
	content 	= models.CharField(max_length=255)
	
	created 	= models.DateTimeField(auto_now_add=True)
	update		= models.DateTimeField(auto_now=True)



	class Meta:
		ordering 			= ('-created',)
		verbose_name		= 'Comment'
		verbose_name_plural = 'Comments'


	def __str__(self):
		return "{0} made a comment on {1}".format(self.user.username,self.post.title)
	

	@property
	def readable_time(self):
		return utils.human_readable_time(self.created)








	

