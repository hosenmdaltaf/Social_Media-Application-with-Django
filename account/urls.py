from django.urls import path
from django.conf import settings

from account.views import (
    ProfileView,
    registration_view,
    login_view,
    logout_view,
    edit_account_view,
 	
)

app_name = 'account'

urlpatterns = [
	#path("", account_view, name="view"),
    
    path('userprofile/',ProfileView.as_view(),name='profile-page'),
    path('<user_id>/edit/',edit_account_view, name="edit"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', registration_view, name="register"),
]