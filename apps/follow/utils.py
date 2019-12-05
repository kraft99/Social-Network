from django.contrib.auth.models import User
from .models import Follow



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


def get_people_user_follows(user):
    """
    Returns a ``QuerySet`` representing the users that the given user follows.
    
    """
    ul = Follow.objects.filter(from_user=user).values_list('to_user', 
        flat=True)
    return User.objects.filter(id__in=ul)


def get_people_following_user(user):
    """
    Returns a ``QuerySet`` representing the users that follow the given user.
    
    """
    ul = Follow.objects.filter(to_user=user).values_list('from_user', 
        flat=True)
    return User.objects.filter(id__in=ul)


def get_mutual_followers(user):
    """
    Returns a ``QuerySet`` representing the users that the given user follows,
    who also follow the given user back.
    
    """
    follows = Follow.objects.filter(from_user=user).values_list('to_user',
        flat=True)
    following = Follow.objects.filter(to_user=user).values_list('from_user',
        flat=True)
    return User.objects.filter(
        id__in=set(follows).intersection(set(following)))


def suggest_user_followers(user,count=4):
    # TODO -> Make it Better (Graph Algorithm)
    # @limited : doesn't work better when auth user unfollows other users.
    """
    QuerySet - Returns suggested users for current users.
    """
    users_followings_qry_id = list(get_people_user_follows(user).values_list('id',flat=True))
    users = User.objects.exclude(id__in = users_followings_qry_id)

    return users.exclude(username__iexact=user.username)[:count]



   


