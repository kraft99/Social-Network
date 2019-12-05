from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest

from apps.account.models import Profile





def ajax_required(f):
    """Not a mixin, but a nice decorator to validate than a request is AJAX"""
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap



def user_is_profile_owner(f):
	def wrap(request,*args,**kwargs):
		profile = Profile.objects.filter(owner__username = kwargs['username']).first()
		if request.user.id == profile.owner.id:
			return f(request,*args,**kwargs)
		else:
			raise PermissionDenied

	wrap.__doc__ = f.__doc__
	wrap.__name__ = f.__name__
	return wrap
