from django.shortcuts import render,redirect, get_object_or_404
from posts.models import Post,Comment
from .forms import PostModelForm,CommentModelForm
from django.urls import reverse_lazy


from django.views.generic import (
    ListView,
    #  DetailView,
     CreateView,
	 UpdateView,
	 DeleteView
)


# Create your views here.
def home(request):


    return render(request,'baseapp/homepage.html',)



# class PostdetailView(DetailView):
#     model=Post
#     template_name='users/detail.html'

def postdetail(request,id):
    details=Post.objects.get(id=id)
    comments=Post.objects.filter()

    comments_form = CommentForm()  

    if request.method == 'POST': 
        comments_form = CommentForm(request.POST ) 
        if comments_form.is_valid(): 
            content = request.POST.get('text') 
            # comment = CommentForm.objects.create(post = Post, user = request.user, content = content) 
            comments_form.save() 
            return redirect("baseapp:details" )
        else: 
            comments_form = CommentForm()    
     
    return render(request,'users/detail.html',{'details':details,'comments':comments})

   

class PostCreateView(CreateView):
    model=Post
    fields= ['image','content']
    template_name='users/post_create_form.html'
    success_url = reverse_lazy("account:profile-page")


    # def form_valid(self,form):
    #     form.instance.writer = self.request.user
    #     return super().form_valid(form)



class PostUpdateView(UpdateView):
    model=Post
    fields= ['title','image','content']
    template_name='baseapp/update_form.html'
    success_url = reverse_lazy("account:profile-page")



class PostDeleteView(DeleteView):
    model=Post
    template_name='baseapp/delete_form.html'
    success_url = reverse_lazy("account:profile-page")



  
# def post_detailview(request, id): 
    
#   if request.method == 'POST': 
#     cf = CommentForm(request.POST or None) 
#     if cf.is_valid(): 
#       content = request.POST.get('content') 
#       comment = Comment.objects.create(post = Post, user = request.user, content = content) 
#       comment.save() 
#       return redirect(Post.get_absolute_url()) 
#     else: 
#       cf = CommentForm() 
        
#     context ={ 
#       'comment_form':cf, 
#       } 
#     return render(request, 'users/add_comment_to_post.html', context)





