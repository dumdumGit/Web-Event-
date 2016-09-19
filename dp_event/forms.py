from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from dp_event.models import Event
from dp_event.models import Visitor

class formevent(forms.Form):
	pilih=(('1','-Jumlah Tiket'),('2','1'),('3','2'),('4','3'),('5','4'),('6','5'))
	jumlah_tiket = forms.ChoiceField(choices=pilih)

class form_login(forms.Form):
	username = forms.CharField(label=(u'username'))
	password = forms.CharField(label=(u'password'))
	
	def saringan(self):
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("Username Telah Digunakan silahkan pilih username lain.")
