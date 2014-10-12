from django import forms
from PeerReviewApp.models import *

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())

class AccountForm(forms.ModelForm):
	class Meta:
		model = SiteUser
		exclude = ('id', 'password','last_login','email',)

class AgreementForm(forms.ModelForm):
	class Meta:
		model = SiteUser
		fields = ('agreed_to_form',)

class SignupForm(forms.ModelForm):
	error_messages = {
		'password_mismatch': 'The two password fields didn\'t match.',
	}
	password = forms.CharField(label='Password', widget=forms.PasswordInput())
	retype_password = forms.CharField(label='Retype Password', widget=forms.PasswordInput(), help_text='Enter the same password as above, for verification.')
	
	class Meta:
		model = SiteUser
		fields = ('email', 'first_name', 'last_name', 'department', 'lab', 'pi')
	
	def clean_retype_password(self):
		password = self.cleaned_data.get('password')
		retype_password = self.cleaned_data.get('retype_password')
		if password and retype_password and password != retype_password:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return retype_password
	
	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class SubmitManuscript(forms.ModelForm):
	class Meta:
		model = Manuscript
		exclude = ('review_period', 'authors', 'reviewers',)