from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from apps.common.decorators import user_is_profile_owner
from django.template.response import TemplateResponse
from django.contrib.auth import views as django_views
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.contrib import auth

from apps.activity.models import Action
from apps.follow.models import Follow
from apps.common import utils

from .forms import (
	LoginForm,
	RegisterForm,
	ProfileEditForm,
)

backend_auth = getattr(settings,'BACKEND_AUTH','django.contrib.auth.backends.ModelBackend')

@login_required
def user_profile(request,username=None):
	if not username is None:
		user = get_object_or_404(get_user_model(),username=username.strip())
		user_followers = Follow.get_people_following_user(user)
		user_followings = Follow.get_people_user_follows(user)
		posts_by_user = user.posts.all()
	else:
		raise Http404
	actions = Action.objects.exclude(user = request.user)
	following_id = list(Follow.get_people_user_follows(user).values_list('id',flat=True))
	if following_id:
		actions = actions.filter(user__id__in = following_id)\
						 .select_related('user','user__profile')\
						 .prefetch_related('target')
	actions = actions[:5] # 5 action objects at a time
	# print(actions)

	ctx = dict()
	ctx['user'] = user
	ctx['user_followers'] = user_followers
	ctx['user_followings'] = user_followings
	ctx['posts'] = posts_by_user
	ctx['actions'] = actions
	return TemplateResponse(request,'profile/profile_index.html',ctx)
	


def account_auth(request):
	if request.user.is_authenticated:
		return redirect('/')
	next = utils.get_next(request)
	if request.method == 'POST':
		if 'register-fm' in request.POST:
			form = RegisterForm(data = request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				phone_number = cd['phone_number']
				username 	 = cd['username']
				full_name 	 = cd['full_name']
				gender    	 = cd['gender']
				password1  	 = cd['password1']
				password2 	 = cd['password2']
				if not (password2 == password1) and len(password2) > 6:
					print('passwords dont match.')
					return redirect('account:auth')
				if get_user_model().objects.filter(username__iexact=username.lower()).exists():
					print('username already taken')
					return redirect('account:auth')
				user = get_user_model().objects.create_user(username = username,email=None,password = password2)
				user.profile.full_name = full_name
				user.profile.phone_number = phone_number
				user.profile.gender = gender
				user.profile.save()
				if not user is None:
					auth.login(request,user,backend=backend_auth)
					return redirect('/')
				else:
					print('error message')
					return redirect('account:auth')
			else:
				print('invalid input')
				return redirect('/')
		elif 'login-fm' in request.POST:
			login_username = request.POST.get('username').strip()
			login_password = request.POST.get('password').strip()
			print(login_username,login_password)
			login_user = auth.authenticate(username=login_username,password=login_password)
			if login_user is not None:
				if login_user.is_active:
					auth.login(request,login_user,backend=backend_auth)
					if next and next != request.path:
						return redirect(next)
					else:
						return redirect('/')
				else:
					print('user account is not active')
					return redirect('account:auth')
			else:
				print('username and password dont match in db.')
				return redirect('account:auth')
	form = RegisterForm()
	ctx = {'form':form}
	return TemplateResponse(request,'account/register.html',ctx)



@login_required
def account_logout(request):
	auth.logout(request)
	#TODO: alert - success message
	return redirect('/')


@login_required
@user_is_profile_owner
def account_edit(request,username):
	if not username is None:
		user = get_object_or_404(get_user_model(),username = username.strip())
		form = ProfileEditForm(instance=user.profile)
		pform = PasswordChangeForm(request.user)
		if request.method == 'POST':
			if 'edit-profile-form' in request.POST:
				profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES) 
				if profile_form.is_valid():
					instance = profile_form.save(commit=False)
					print(instance.pic)
					instance.save()
				else:
					print('error')
			elif 'change-password-form' in request.POST:
				pform = PasswordChangeForm(request.user,request.POST)
				if pform.is_valid():
					user_instance = pform.save(commit = True)
					update_session_auth_hash(request,user_instance)
					print('successfully changed password')
				else:
					print('data invalid')
			else:
				pass
			return redirect(reverse('account:profile-edit',kwargs={'username':request.user.username}))
	ctx = dict()
	ctx['user'] = user
	ctx['form'] = form
	ctx['pform'] = pform
	return TemplateResponse(request,'profile/profile_edit.html',ctx)
