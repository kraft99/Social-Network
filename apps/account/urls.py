from django.urls import path
from .import views




app_name = 'account'

urlpatterns = [
    path('auth/',views.account_auth,name='auth'),
    path('auth/logout/',views.account_logout,name='logout'),
    
	path('profile/<str:username>/',views.user_profile,name='user-profile'),
	path('profile/<str:username>/edit/',views.account_edit,name='profile-edit'),

]

