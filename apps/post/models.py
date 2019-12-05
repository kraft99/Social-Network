from django.utils import timezone

from apps.common.utils import photo_file_loc,human_readable_time

from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.http import Http404
from django.conf import settings
from django.urls import reverse

from django.db import models



class Post(models.Model):

	owner					= models.ForeignKey(to=settings.AUTH_USER_MODEL,
												related_name='posts',
												on_delete=models.CASCADE)

	title 					= models.CharField(max_length=125,blank=True,null=True)
	content					= models.TextField(max_length=250)
	slug 					= models.SlugField(max_length=125,unique=True,null=True,blank=True)
	photo					= models.ImageField(upload_to=photo_file_loc,blank=True,null=True,default='')

	users_like				= models.ManyToManyField(to=settings.AUTH_USER_MODEL,
													related_name='post_liked',
													blank=True)
	total_likes				= models.PositiveSmallIntegerField(default=0)
	views 					= models.PositiveSmallIntegerField(default=0,blank=True,null=True)

	created					= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)


	class Meta:
		ordering 			= ('-created',)
		verbose_name		= 'Post'
		verbose_name_plural = 'Posts'


	def __str__(self):
		return '{0}'.format(self.title)


	@property
	def get_absolute_url(self):
		return reverse('post:post-view',args=[str(self.slug)])
	

	@property
	def created_by(self):
		return self.owner.username
	

	@property
	def created_at(self):
		return human_readable_time(self.created)


	@property
	def pic(self):
		if self.photo:
			return self.photo.url
		return

	pic_url = pic


	@property
	def comments_count(self):
		return self.comments.count() if self.comments else 0


	@property
	def recent_post_comment(self):
		qry = self.comments.first()
		return qry

	@property
	def more_comments(self):
		qry = self.comments.all()
		if qry.exists():
			if qry.count() > 1:
				return True
			elif qry.count() == 1:
				return False
		return False
	


	@property
	def likes_count(self):
		return self.total_likes


	@property
	def post_users_like(self):
		return self.users_like.all()
	
	
	