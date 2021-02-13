from django.urls import path
from django.conf import settings

from account.views import (

    registration_view,
    login_view,
    logout_view,
    edit_account_view,
   # account_view,
   ProfileView,

   PostdetailView,
   PostCreateView,
   PostUpdateView,
   PostDeleteView,	
)

app_name = 'account'

urlpatterns = [
	#path("", account_view, name="view"),
    path('',ProfileView.as_view(),name='profile-page'),
	path('<user_id>/edit/',edit_account_view, name="edit"),
    path('post/<int:pk>',PostdetailView.as_view(),name='articale-detail'),
    path('post/update/<int:pk>',PostUpdateView.as_view(),name='articale-update'),
    path('post/new',PostCreateView.as_view(success_url='/'),name='post-create'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='articale-delete'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', registration_view, name="register"),
]