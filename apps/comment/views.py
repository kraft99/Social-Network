from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods
from apps.common.decorators import ajax_required
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.urls import reverse

from apps.comment.models import Comment
from apps.activity.models import Action
from apps.post.models import Post
from apps.activity import utils




@ajax_required
@require_http_methods(["POST"])
def comment_add(request):
	post_id = request.POST.get('post_id');
	post    = get_object_or_404(Post,id = post_id)
	user = request.user
	comment_text = request.POST.get('comment_text'); 
	comment_obj,added = Comment.objects.get_or_create(user=user,
													post=post,
													content=comment_text)
	comment_added = False
	if added:
		comment_added = True
		utils.create_action(user,'commented on',post)
	count = post.comments_count
	data = {'comment_added':comment_added,'comments_count':count}
	return JsonResponse(data)