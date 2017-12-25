from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class ContactForm(forms.Form):
	fullname= forms.CharField(widget=forms.TextInput(
		attrs={
		"class":"form-control",
		"id":"form_full_name",
		"placeholder":"Enter Your Full Name"
		}
		)
	)
	email =forms.EmailField(widget=forms.EmailInput(
		attrs={
		"class":"form-control",
		"id":"form_full_name",
		"placeholder":"E-mail"
		}
		)
	)
	content=forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class":"form-control",
			"placeholder":"Your message"
			}
			)
		)


	def clean_email(self):
		email=self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be Gmail")
		return email

class LoginForm(forms.Form):
	username=forms.CharField()
	
	password=forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username=forms.CharField()
	email =forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
	def clean_username(self):
		username=self.cleaned_data.get("username")
		un=User.objects.filter(username=username)
		if un.exists():
			raise forms.ValidationError("Username is take")
		return username
	def clean_email(self):
		email=self.cleaned_data.get("email")
		un=User.objects.filter(email=email)
		if un.exists():
			raise forms.ValidationError("email is take")
		return email
	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Passwords must match")
		return data