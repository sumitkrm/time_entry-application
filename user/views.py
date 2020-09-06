from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm, NewTaskForm
from django.template import Context 
from .models import UserTaskList
from django.db.models import Q


def index(request):
	if request.method == 'POST': 
		task_name = request.POST.get('task_name', "null")
		project_name = request.POST.get('project_name', "null")
		start_time = request.POST.get('start_time', "null")
		end_time = request.POST.get('end_time', "null")
		print(task_name, project_name, start_time, end_time)
	
		task_info = UserTaskList(user_id = request.user.id, task_name = task_name, project_name = project_name, start_time = start_time, end_time = end_time)
		task_info.save()


	content = {}
	current_user = request.user
	content['title'] = 'Time Chart'
	content['first_name'] = current_user.first_name
	content['user_data'] = UserTaskList.objects.filter(Q(user_id=int(current_user.id))).values()
	return render(request, 'user/index.html', content) 
	#eturn render(request, 'user/index.html', {'title':'time_chart', 'user_id':current_user.id}) 


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
