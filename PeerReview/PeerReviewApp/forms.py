from django import forms
from PeerReviewApp.models import *

SCHOOLS = (
	'Goizueta Business School',
	'Laney Graduate School',
	'School of Law',
	'Schoolf of Medicine',
	'Nell Hodgson Woodruff School of Nursing',
	'Rollins School of Public Health',
	'Candler School of Theology',
	'College of Arts and Sciences',
	'Other',
)

class LoginForm(forms.Form):
	''' On log in, you only need an email and a password '''
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emory Email Address'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class AccountForm(forms.ModelForm):
	''' This is a pythonic way of changing a single user's settings ''' 
	def __init__(self, *args, **kwargs):
		super(AccountForm, self).__init__(*args, **kwargs)
		try:
			has_agreed = self.instance.agreed_to_form
		except AttributeError:
			has_agreed = True
		if has_agreed:
			self.fields['agreed_to_form'].widget = forms.widgets.HiddenInput()
		
	class Meta:
		model = SiteUser
		exclude = ('id', 'password','last_login','email',)

class AgreementForm(forms.ModelForm):
	''' This is for just the agreement form. It allows the logged in
		user to agree with the Terms of Service document '''
	class Meta:
		model = SiteUser
		fields = ('agreed_to_form',)

class SignupForm(forms.ModelForm):
	''' This is the main sign-up form '''
	error_messages = { # Add errors here
		'password_mismatch': 'The two password fields didn\'t match.',
	}
	# Form needs two passwords to make sure the user doesn't mistype
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-center', 'placeholder': 'Enter your Password'}), label='Password', help_text='Choose a password')
	retype_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-center', 'placeholder': 'Re-enter your password, for verification'}), label='Retype Password', help_text='Enter the same password as above, for verification.')
	
	class Meta:
		model = SiteUser
		# These are the fields that the user needs to input when they create their account
		fields = ('email', 'first_name', 'last_name', 'department', 'lab', 'pi', 'school')
		widgets = {
			'email': forms.EmailInput(attrs={'class': 'form-control text-center', 'placeholder': 'Emory Email Address'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Last Name'}),
			'department': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Department'}),
			'lab': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Name of Lab'}),
			'pi': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Name of Primary Investigator'}),
			'school': forms.Select(attrs={'class': 'form-control text-center', 'placeholder': 'Choose your School'}),
		}
	
	# This method validates that the two passwords are the same
	# If they don't match it throws an error
	def clean_retype_password(self):
		password = self.cleaned_data.get('password')
		retype_password = self.cleaned_data.get('retype_password')
		if password and retype_password and password != retype_password:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return retype_password
	
	# This is the method for saving the newly created user
	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class SubmitManuscript(forms.ModelForm):
	''' Submitting a manuscript '''
	def __init__(self, *args, **kwargs):
		super(SubmitManuscript, self).__init__(*args, **kwargs)
	
	# This is the method for saving the newly created user
	def save(self, review_period, authors, commit=True):
		manuscript = super(SubmitManuscript, self).save(commit=False)
		manuscript.review_period = review_period
		if commit:
			manuscript.save()
		if type(authors) is list:
			manuscript.authors = authors
		else:
			manuscript.authors = [authors]
		if commit:
			manuscript.save()
		return manuscript
	
	class Meta:
		model = Manuscript
		exclude = ('review_period', 'authors', 'reviewers','review_file')
