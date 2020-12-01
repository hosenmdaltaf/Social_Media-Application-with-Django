from django.shortcuts import render,redirect, get_object_or_404
from baseapp.models import Post,Comment
from .forms import CommentForm 


# Create your views here.
def home(request):
   
    
    return render(request,'baseapp/homepage.html',)


  
def post_detailview(request, id): 
    
  if request.method == 'POST': 
    cf = CommentForm(request.POST or None) 
    if cf.is_valid(): 
      content = request.POST.get('content') 
      comment = Comment.objects.create(post = Post, user = request.user, content = content) 
      comment.save() 
      return redirect(Post.get_absolute_url()) 
    else: 
      cf = CommentForm() 
        
    context ={ 
      'comment_form':cf, 
      } 
    return render(request, 'users/add_comment_to_post.html', context)




