from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from dp_event.models import Event
from dp_event.models import Visitor
import warnings


class form_login(forms.Form):
	username = forms.CharField(label=(u'username'))
	password = forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=False))
	

class form_daftar(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("First Name "))
	last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("Last Name  "))
	CHOICES=[('laki-laki','laki-laki'),('perempuan','perempuan')]
         
	jk = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("Email Address  "))
	no_ktp = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("No KTP  "))
	kota = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("Kota  "))
	alamat = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':30}))
	telepon = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)),label=("No Telepon  "))
	telepon2 = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)),label=("No Telepon ke-2  "))
	foto = forms.FileField()

class form_username(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)), label=("Username  "))		
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30)),label=("Password  "))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.Objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("Username telah digunakan,Silahkan Pilih lagi username lain :)")	
	
	def clean_password(self):
		if self.cleaned_data['password'] != self.cleaned_data['password']:
			raise forms.ValidationError("Password tidak sesuai,Silahkan Coba lagi :)")
		return self.cleaned_data

