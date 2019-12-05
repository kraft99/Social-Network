from django.contrib.auth import get_user_model


def is_auth(request):
	flag = None
	if not request.user.is_authenticated:
		flag = False
	if not isinstance(request.user,get_user_model()):
		flag = False
	if not (request.user.is_staff or request.user.is_superuser or request.user.is_active):
		flag = False
	else:
		flag = True
	return {'is_auth':flag}
