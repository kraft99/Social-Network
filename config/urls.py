from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_view,name='index'),
    path('oauth/',include('social_django.urls',namespace='social')),
    path('account/',include('apps.account.urls',namespace='account')),
    path('comment/',include('apps.comment.urls',namespace='comment')),
    path('follow/',include('apps.follow.urls',namespace='follow')),
    path('search/',include('apps.search.urls',namespace='search')),
    path('post/',include('apps.post.urls',namespace='post')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# handler404 = TemplateView.as_view(template_name='404.html')
# handler400 = TemplateView.as_view(template_name='400.html')
# handler500 = TemplateView.as_view(template_name='500.html')
# handler403 = TemplateView.as_view(template_name='403.html')
