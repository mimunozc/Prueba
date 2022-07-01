from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name =forms.CharField(label='Nombre',required=True)
	last_name =forms.CharField(label='Apellido',required=True)
	username = forms.CharField(label='Usuario',required=True)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
	
 	

	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
	
	def save(self,commit=True):
		user = super(UserRegisterForm,self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


