from django.conf import settings
from apps.post.models import Post
from django.db import models


User = settings.AUTH_USER_MODEL


class Report(models.Model):
	OPTION_1 = 1
	OPTION_2 = 2
	OPTION_3 = 3

	OPTIONS = (
		(OPTION_1,('option 1')),
		(OPTION_2,('option 2')),
		(OPTION_3,('option 3')),
	)

	user 		= models.ForeignKey(to=User,related_name='report_by',on_delete=models.CASCADE)
	post 		= models.ForeignKey(to=Post,related_name='reports',on_delete=models.CASCADE)
	status 		= models.PositiveSmallIntegerField(choices=OPTIONS,blank=True,null=False)

	created		= models.DateTimeField(auto_now_add=True)


	class Meta:
		unique_together 	= (('user','post'),)
		ordering			= ('-created',)
		verbose_name		= 'Report'
		verbose_name_plural = 'Reports'


	def __str__(self):
		return self.user.username
