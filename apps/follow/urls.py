from django.urls import path
from .import views




app_name = 'follow'

urlpatterns = [
    path('toggle/',views.follow_toggle,name='follow-toggle'),
]

