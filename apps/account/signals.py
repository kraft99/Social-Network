from apps.common.random_avatar import user_random_avatar
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,post_delete
from django.contrib.auth.models import User
from .models import Profile



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
# @purpose : create a new profile for any new user created
    if created:
        Profile.objects.create(owner = instance)
        
          

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
# @purpose : save old profile for user objects,anytime save is invoked.
    instance.profile.save()



@receiver(pre_save,sender=Profile)
def pre_save_code_receiver(sender,instance,*args,**kwargs):
# @purpose : assign code to user code field,on save
    if not instance.pic:
        instance.pic = user_random_avatar() # assign random avatar pic to user profile model.