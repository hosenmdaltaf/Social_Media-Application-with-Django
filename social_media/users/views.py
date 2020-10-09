from django.shortcuts import render
from .models import Profile

def profiles(request):
    return render (request,'users/profile.html')