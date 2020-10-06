from django.shortcuts import render
from .models import Post
from .models import Profile

# Create your views here.
def home(request):
    obj=Post.objects.all()
    return render(request,'baseapp/home.html',{'obj':obj})

def profiles(request):
    obj=Profile.objects.all()
    return render(request,'baseapp/profile.html',{'obj':obj})
