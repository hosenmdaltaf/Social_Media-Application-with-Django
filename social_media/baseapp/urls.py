from django.urls import path
from .import views

app_name='baseapp'

urlpatterns=[
    path('',views.home,name='home-page'),
   
]