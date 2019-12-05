from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib.auth import views as django_views
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages

from apps.follow.models import Follow
from apps.post.models import Post
from apps.follow.utils import *



def index_view(request):

	# TODO : Find a better way of implementing feeds.

	posts_feeds = None
	if request.user.is_authenticated:
		user = request.user
		user_followers_list_id = list(Follow.get_people_following_user(user).values_list('id',flat=True))
		user_followings_list_id = list(Follow.get_people_user_follows(user).values_list('id',flat=True))
		feeds_user_list = user_followings_list_id + user_followers_list_id + [user.id]

		if len(feeds_user_list) < 3: 
			posts_feeds = Post.objects.all()
		else:
			posts_feeds = Post.objects.filter(owner__id__in = feeds_user_list)
	else:
		# Is Anonymous user
		posts_feeds = Post.objects.all()

	posts = posts_feeds
	paginator = Paginator(posts, 6) 
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		posts = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return TemplateResponse(request,'post/index_ajax.html',{'posts':posts})

	# suggested users
	users_suggested_users = get_user_model().objects.none()
	if request.user.is_authenticated:
		users_suggested_users = suggest_user_followers(request.user)

	ctx = {}
	ctx['posts'] = posts
	ctx['suggested_users'] = users_suggested_users
	return TemplateResponse(request,'index.html',ctx)

