from django.utils import timezone
import datetime

from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user,verb,target=None):
    now = timezone.now()
    last_min = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user__id=user.id,verb=verb,created__gte=last_min)
    
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct,target_id=target.id)

    if not similar_actions:
        action_obj = Action(user=user, verb=verb, target=target)
        action_obj.save()
        return True
    return False
