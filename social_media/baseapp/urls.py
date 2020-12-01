from django.urls import path

from .import views

app_name='baseapp'

urlpatterns=[
    path('',views.home,name='home-page'),
    path('post_detailview/<int:pk>/comment/', views.post_detailview, name='comment')
      
   
]