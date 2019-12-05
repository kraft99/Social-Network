from apps.common.slug_generator import unique_slug_generator
from django.db.models.signals import pre_save,m2m_changed
from django.dispatch import receiver
from .models import Post



@receiver(pre_save,sender=Post)
def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


@receiver(m2m_changed, sender=Post.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()