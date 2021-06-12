from django.urls import path

from .import views

from baseapp.views import (

#    PostdetailView,
   PostCreateView,
   PostUpdateView,
   PostDeleteView,	
)

app_name='baseapp'

urlpatterns=[
    path('',views.home,name='home-page'),
    path('post/<int:id>',views.postdetail,name='articale-detail'),

    # path('post/<int:pk>',PostdetailView.as_view(),name='articale-detail'),
    path('post/update/<int:pk>',PostUpdateView.as_view(),name='articale-update'),
    path('post/new',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='articale-delete'),

    # path('post_detailview/<int:pk>/comment/', views.post_detailview, name='comment')
      
   
]