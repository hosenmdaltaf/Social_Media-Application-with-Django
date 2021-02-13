from django.shortcuts import render




'''

 model = Post 
      paginate_by = 2
      context_object_name = 'posts'
      template_name = 'profile.html'
      ordering = ['title']
def profiles(request,pk):
    posts =Post.objects.all()

    return render(request,'users/profile.html',{'posts':posts})

      from django.views.generic import (
    ListView,
     DetailView,
     CreateView
)
class PostsView(ListView):
    model = Post 
    
    context_object_name = 'posts'
    template_name = 'profile.html'
   
    print(context_object_name )


'''
