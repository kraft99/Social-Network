from django.urls import path
from .import views




app_name = 'post'

urlpatterns = [
    path('like-unlike/',views.post_like_unlike,name='post-like-unlike'),
    path('add/',views.post_add,name='post_add'),
    path('detail/<str:slug>/',views.post_view,name='post-view'),
    path('delete/<str:slug>/',views.post_delete,name='post-delete'),
]

