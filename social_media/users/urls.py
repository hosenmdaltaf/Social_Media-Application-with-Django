from django.urls import path
from .import views


app_name='users'

urlpatterns =[
     path('profiles/',views.profiles,name='profile-page'),
    
]