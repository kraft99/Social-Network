from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied
from apps.common.decorators import ajax_required
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse

from apps.follow.models import Follow
from apps.post.models import Post
from apps.activity import utils




@ajax_required
@require_http_methods(["POST"])
def follow_toggle(request):
	#NOTE: Refactor this !
	username = request.POST.get('to_user__username')
	from_user = request.user
	try:
		to_user = get_user_model().objects.get(username__iexact=username)
		from_user = get_user_model().objects.get(id=from_user.id)
	except get_user_model().DoesNotExist:
		raise Http404
	follow_obj,created = Follow.objects.get_or_create(to_user=to_user,
														from_user=from_user)
	is_follow = True
	if not created:
		follow_obj.delete()
		is_follow = False
	else:
		utils.create_action(from_user,'is now following',to_user)
	data = {'is_follow':is_follow}
	return JsonResponse(data)