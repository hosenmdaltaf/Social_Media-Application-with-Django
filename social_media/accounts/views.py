
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def register(request):
    #user register form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
            #log in user
           login(request,user)
           return redirect('accounts:login')
    else:
        form=UserCreationForm()

    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            return redirect( 'baseapp:home-page')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:logout')
    return render(request,'accounts/logout.html')

