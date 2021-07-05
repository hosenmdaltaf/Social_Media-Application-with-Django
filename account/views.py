from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from account.forms import AccountAuthenticationForm, RegistrationForm,AccountUpdateForm
from django.contrib import messages

from django.conf import settings
from django.contrib.auth.models import User

from account.models import Account
from posts.models import Post
from posts.forms import PostModelForm

import random


from django.views.generic import (
    DetailView
)

'''
def profiles(request):
	data =Post.objects.all()
	paginate_by = 2
	ordering = ['post_date']
	return render(request,'account/account.html',{'data':data})

	'''
def Userfeed(request):
	
    allposts=Post.objects.all()
    # details=Post.objects.get(id=id)

    # posts_form  = PostModelForm()  

    # if request.method == 'POST': 
    #     posts_form = PostModelForm(request.POST ) 
    #     if posts_form.is_valid(): 
    #         content = request.POST.get('content') 
	# 		# image = request.POST.get('image') 
    #         # comment = PostModelForm.objects.create(post = Post, user = request.user, content = content) 
    #         posts_form .save() 
    #         return redirect("baseapp:details" )
    #     else: 
    #         posts_form  = PostModelForm()    


	 # initials
    p_form = PostModelForm()

    post_added = False

    # profile = Account.objects.get(user=request.user)
    # profile= self.request.usersettings.AUTH_USER_MODEL
    profile = request.user


    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = PostModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.writer = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True 

    # ppp= Account.objects.all()

    profiles = []
    all_posts = list(Account.objects.all())
    # random_post_number = post_number - len(profiles)
    # random_posts = random.sample(all_posts, random_post_number)
    random_posts = random.sample(all_posts, 3)
    for random_post in random_posts:
        profiles.append(random_post)

    # return post_objects
  


    context = {
        'allposts': allposts,
        'p_form': p_form,
		'profiles': profiles,

		'post_added': post_added,
    }

    return render(request, 'users/userfeed.html', context)


class ProfileDetailView(DetailView):
    model = Account
    context_object_name = 'my_profile'
    template_name = 'account/account.html' 

    def get_object(self,**kwargs):
        pk= self.kwargs.get('pk')
        view_profile = Account.objects.get(pk=pk)
        return view_profile



def edit_account_view(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login")
	user_id = kwargs.get("user_id")
	account = Account.objects.get(pk=user_id)
	if account.pk != request.user.pk:
		return HttpResponse("You cannot edit someone elses profile.")
	context = {}
	if request.POST:
			form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
			if form.is_valid():
				form.save()
				new_username = form.cleaned_data['username']
				return redirect("account:profile-page")
			else:
				form = AccountUpdateForm(request.POST, instance=request.user,
					initial={
						"id": account.pk,
						"email": account.email,
						"username": account.username,
						"profile_image": account.profile_image,
						"hide_email": account.hide_email,
						"bio": account.bio,
						"full_name": account.full_name,
					}
				)
				context['form'] = form
	else:
		form = AccountUpdateForm(
			initial={
					"id": account.pk,
					"email": account.email,
					"username": account.username,
					"profile_image": account.profile_image,
					"bio": account.bio,
					"full_name": account.full_name,
				}
			)
		context['form'] = form
	context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
	return render(request, "account/edit_account.html", context)



def registration_view(request, *args, **kwargs):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			# email = form.cleaned_data.get('email')
			# raw_password = form.cleaned_data.get('password1')
			# accounts = authenticate(email=email, password=raw_password)
			# login(request, accounts)
			return redirect('account:login')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def login_view(request, *args, **kwargs):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("account:profile-page")

	 if request.POST:
	 	form = AccountAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			return redirect("account:profile-page")

	 else:
	 	form = AccountAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'account/login.html', context)

def logout_view(request, *args, **kwargs):
    logout(request)

    return render(request,'account/logout.html')
