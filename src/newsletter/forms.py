from django import forms

from .models import SignUp

class ContactForm(forms.Form): #more customizable than below
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split('@')
	# 	domain, extension = provider.split('.')
	# 	if not extension == 'edu':
	# 		raise forms.ValidationError("please use a valid .edu email address")
	# 	return email



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = [
			'full_name',
			'email'
		]
		# exclude = ['full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("please use USC email")
		if not extension == 'edu':
			raise forms.ValidationError("please use a valid .edu email address")
		return email
		# if not ".edu" in email:
		# 	raise forms.ValidationError("please use a valid .edu email address")
		# return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')

		return full_name
