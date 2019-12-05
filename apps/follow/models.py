from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import Http404
from django.db import models


User = get_user_model()


class Follow(models.Model):
	''' Follow Model. '''
	to_user					= models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='followers')
	from_user				= models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='followings')

	created					= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now = True)

	class Meta:
		unique_together 	= (('to_user','from_user'),)
		ordering 			= ('-created',)


	def save(self,*args,**kwargs):
		is_self = self.to_user == self.from_user
		if is_self:
			raise ValueError('You can\t follow yourself')
		return super(Follow,self).save(*args,**kwargs)


	def __str__(self):
		return "{0} is following {1}".format(self.from_user.username,self.to_user.username)


	@classmethod
	# current user followings
	def get_people_user_follows(cls,user):
		user_followings = cls.objects.filter(from_user=user).values_list('to_user',flat=True)
		return User.objects.filter(id__in=user_followings)
		

	@classmethod
	# current users followers
	def get_people_following_user(cls,user):
		user_followers = cls.objects.filter(to_user=user).values_list('from_user',flat=True)
		return User.objects.filter(id__in=user_followers)


	@classmethod
	# both sides follow each other
	def get_mutual_followers(cls,user):
		follows = cls.objects.filter(from_user=user).values_list('to_user',
			flat=True)
		following = cls.objects.filter(to_user=user).values_list('from_user',
			flat=True)
		return User.objects.filter(
			id__in=set(follow).intersection(set(following)))



	# @classmethod
	# def switch_follow(cls,to_user,from_user):
	# 	# toggle follow & unfollow
	# 	# from_user is the current login user performing action on to_user.
	# 	if to_user == from_user:
	# 		raise ValueError('You can\t follow yourself')
	# 	try:
	# 		to_user = get_user_model().objects.get(id=to_user.id)
	# 		from_user = get_user_model().objects.get(id=from_user)
	# 	except get_user_model().DoesNotExist:
	# 		raise Http404
			
	# 	ctx = dict()
	# 	is_follow = None
	# 	f_obj,created = cls.objects.get_or_create(to_user=to_user,
	# 		from_user=from_user)
	# 	if not created:
	# 		is_follow = False
	# 		f_obj.delete()
	# 	else:
	# 		is_follow = True
	# 	ctx['is_follow'] = is_follow
	# 	return ctx
