from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from account.forms import AccountAuthenticationForm, RegistrationForm,AccountUpdateForm
from django.contrib import messages

from django.conf import settings

from account.models import Account
from baseapp.models import Post

from django.views.generic import (
    ListView
)

'''
def profiles(request):
	data =Post.objects.all()
	paginate_by = 2
	ordering = ['post_date']
	return render(request,'account/account.html',{'data':data})

	'''


class ProfileView(ListView):
	model = Post
	# paginate_by = 5
	ordering = ['-post_date']
	context_object_name = 'allposts'
	# template_name = 'users/profile.html'
	template_name = 'users/userfeed.html'
	
	def get_context_data(self,*args,**kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['latest']= Post.objects.order_by('-post_date')[:3]
            return context


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
