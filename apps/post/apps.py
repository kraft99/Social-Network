from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'apps.post'

    def ready(self):
    	import apps.post.signals
