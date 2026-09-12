from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	mobile = forms.CharField(max_length=10,required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "mobile", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.mobile = self.cleaned_data['mobile']
		if commit:
			user.save()
		return user



class ProfileForm(UserCreationForm):
	bio = forms.CharField(required=True)
	relationship = forms.CharField(required=True)
	region = forms.CharField(required=True)
	state = forms.CharField(required=True)
	country = forms.CharField(required=True)
	academicbackground = forms.CharField(required=True)
	address_line_2 = forms.CharField(required=True)


	class Meta:
		model = UserProfile
		fields = ("bio" , "relationship", "region" , "country" , "state" , "academicbackground" , "school_name" , "address", "address_line_2" )

	def save(self, commit=True):
		user = super(ProfileForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.bio = self.cleaned_data['bio']
		user.relationship = self.cleaned_data['relationship']
		user.school_name = self.cleaned_data['school_name']
		user.address_line_2 = self.cleaned_data['address_line_2']
		user.region = self.cleaned_data['region']
		user.country = self.cleaned_data['country']
		user.state = self.cleaned_data['state']
		

		if commit:
			user.save()
		return user