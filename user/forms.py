from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 


class UserRegisterForm(UserCreationForm): 
	email = forms.EmailField() 
	phone_no = forms.CharField(max_length = 20) 
	first_name = forms.CharField(max_length = 20) 
	last_name = forms.CharField(max_length = 20)
	password1 = forms.PasswordInput()
	password2 = forms.PasswordInput()
	class Meta: 
		model = User 
		fields = [ 'first_name', 'last_name', 'username', 'email', 'phone_no','password1', 'password2'] 


class NewTaskForm(forms.Form):
	task_name = forms.CharField(max_length = 50)
	project_name = forms.CharField(max_length = 50)
	start_time = forms.DateTimeField
	end_time = forms.DateTimeField