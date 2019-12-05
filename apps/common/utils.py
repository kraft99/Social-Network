import os
import uuid
import random
from PIL import Image

from django.contrib.humanize.templatetags import humanize
from django.core.exceptions import ValidationError
from django.conf import settings


def get_next(request):
    """
    1. If there is a variable named ``next`` in the *POST* parameters, the
    view will redirect to that variable's value.
    2. If there is a variable named ``next`` in the *GET* parameters, the 
    view will redirect to that variable's value.
    3. If Django can determine the previous page from the HTTP headers, the 
    view will redirect to that previous page.
    
    """
    return request.POST.get('next', request.GET.get('next', 
        request.META.get('HTTP_REFERER', None)))


def photo_file_loc(instance,file_obj):
	file_ext = file_obj.split('.')[-1]
	file_obj = '{}.{}'.format(uuid.uuid4().hex[:8],file_ext)
	return os.path.join("photos",instance.owner.username,file_obj)



def human_readable_time(datetime_object = None):
	if not datetime_object:
		return
	return humanize.naturaltime(datetime_object)



def profile_dp(instance,file_obj):
    file_ext = file_obj.split('.')[-1].lower()
    file = '{}.{}'.format(instance.owner.username,file_ext)
    return os.path.join('dp',file)




def default_avatar_url():
    if hasattr(settings,'DEFAULT_AVATAR_PATH'):
        return getattr(settings,'DEFAULT_AVATAR_PATH')
    return
