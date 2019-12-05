from django.db import models
from django.conf import settings
from apps.common.utils import human_readable_time
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    """   Action Model  

    Examples:
        * A user posted a feed
        * A user likes/unlikes a feed
        * A user creates an acoount
        * A user follows/unfollows another user
        * A user comments on a feed
      
    """
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='actions',on_delete=models.CASCADE)
    verb        = models.CharField(max_length = 255)

    target_ct   = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj',on_delete=models.CASCADE)
    target_id   = models.PositiveIntegerField(null=True,blank=True)
    target      = GenericForeignKey('target_ct','target_id')

    created     = models.DateTimeField(auto_now_add=True)


    class Meta:
    	ordering 	= ('-created',)


    @property
    def human_readable(self):
        return human_readable_time(self.created)
    