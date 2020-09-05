from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm
from django.template import Context 

def index(request): 
	current_user = request.user
	print(current_user.id)
	return render(request, 'user/index.html', {'title':'time_chart', 'user_id':current_user.id}) 


def register(request): 
	if request.method == 'POST': 
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() 
			username = form.cleaned_data.get('username') 
			email = form.cleaned_data.get('email')
			print(form.cleaned_data.get('first_name'))
			first_name = form.cleaned_data.get('first_name') 
			last_name = form.cleaned_data.get('last_name')
			return redirect('login') 
	else: 
		form = UserRegisterForm() 
	return render(request, 'user/register.html', {'form': form, 'title':'reqister here'}) 

def Login(request): 
	if request.method == 'POST':
		username = request.POST['username'] 
		password = request.POST['password'] 
		user = authenticate(request, username = username, password = password) 
		if user is not None: 
			form = login(request, user) 
			messages.success(request, f' welcome {username} !!') 
			return redirect('index') 
		else: 
			messages.info(request, f'username and/or password is incorrect') 
	form = AuthenticationForm() 
	return render(request, 'user/login.html', {'form':form, 'title':'log in'}) 


def time_chart(request):
	current_user = request.user
	return render(request, 'user/login.html', {'form':form, 'title':'time_chart'}) 
