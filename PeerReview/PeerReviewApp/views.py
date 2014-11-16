import re
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404

from PeerReviewApp.models import *
from PeerReviewApp.forms import *

def index(request):
	''' Main landing page '''
	context = {}
	return render(request, 'index.html', context)

def terms(request):
	''' Terms of service agreement '''
	context = {}
	return render(request, 'terms.html', context)

def auth_login(request):
	context = {}
	context['next'] = request.GET.get('next', False)
	if request.method == 'POST': form = LoginForm(request.POST)
	else: form = LoginForm()
	if form.is_valid() and 'email' in form.cleaned_data and 'password' in form.cleaned_data:
		print 'hit 2'
		user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
		if user is not None:
			login(request, user)
			if request.POST.get('next',False):
				return HttpResponseRedirect(request.POST.get('next', False))
			else:
				return HttpResponseRedirect(reverse('index')) # Redirect to homepage when the user logs in
		else:
			context['errors'] = 'Authentication failed.'
	context['form'] = form
	return render_to_response('login.html', context, context_instance=RequestContext(request))

def signup(request):
	context = {}
	if request.method == 'POST': form = SignupForm(request.POST)
	else: form = SignupForm()
	if form.is_valid():
		context['form'] = form
		# Passwords don't match
		if form.cleaned_data['password'] != form.cleaned_data['retype_password']:
			context['errors'] = 'The passwords you entered do not match.'
			return render(request, 'signup.html', context)

		# Not an Emory email address
		if form.cleaned_data['email'][-10:] != '@emory.edu':
			context['errors'] = 'Sorry! This service is only available within Emory University.'
			return render(request, 'signup.html', context)

		# A user already exists with this email
		if SiteUser.objects.filter(email=form.cleaned_data['email']).count():
			context['errors'] = 'A user already exists with this email.'
			return render(request, 'signup.html', context)

		# Create the new user
		'''
			If we are going to add email authentication, this would be the place to add it.
			I believe this requires messing around with some Django stuff though, so I'm
			going to leave it for later.
		'''
		email = form.cleaned_data['email']
		password = form.clean_retype_password()
		form.save()
		user = authenticate(email=email, password=password)
		login(request, user) # Log the user in
		return HttpResponseRedirect(reverse('index')) # Redirect them to the home page
	context['form'] = form
	return render(request, 'signup.html', context)

@login_required
def agreement(request):
	''' Agree to the form '''
	context = {}
	user = SiteUser.objects.get(email=request.user.email)
	if request.GET.get('next', False):
		context['next'] = request.GET.get('next', False)
	if request.POST:
		if 'delete' in request.POST and request.POST['delete'] == 'DELETE':
			logout(request)
			user.delete()
			return HttpResponseRedirect(reverse('index'))
		form = AgreementForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			if request.POST.get('next',False):
				return HttpResponseRedirect(request.POST.get('next', False))
			else:
				return HttpResponseRedirect(reverse('index'))
			context['errors'] = 'Information saved.'
	else:
		form = AgreementForm(instance=user)
	context['form'] = form
	return render(request, 'agreement.html', context)

@login_required
def auth_logout(request):
	context = {}
	logout(request)
	return render(request, 'logout.html', context)

def has_agreed(user):
	if user.is_authenticated():
		return user.agreed_to_form
	else:
		return False

@user_passes_test(has_agreed, login_url='/agreement/')
def reviewer_home(request):
	context = {}
	return render(request, 'reviewer_home.html', context)

@user_passes_test(has_agreed, login_url='/agreement/')
def browse_manuscripts(request, current_page):
	context = {}
	all_manuscripts = Manuscript.objects.all()
	paginator = Paginator(all_manuscripts, 10)

	try:
		page = paginator.page(current_page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)

	context['page'] = page
	return render(request, 'browse_manuscripts.html', context)

@user_passes_test(has_agreed, login_url='/agreement/')
def assigned_manuscripts(request,current_page):
	context = {}
	manuscripts_assigned = Manuscript.object.get(reviewers=request.user.email)
	context['manuscript_assigned'] = manuscripts_assigned
	return render(request, 'manuscript_assigned.html', context)

@user_passes_test(has_agreed, login_url='/agreement/')
def uploader_home(request):
	context = {}
	return render(request, 'uploader_home.html', context)

@login_required
def account(request):
	context = {}
	user = SiteUser.objects.get(email=request.user.email)
	if 'delete' in request.GET:
		logout(request)
		user.delete()
		return HttpResponseRedirect(reverse('index'))
	if request.POST:
		form = AccountForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			context['errors'] = 'Information saved.'
	else:
		form = AccountForm(instance=user)
	context['form'] = form
	return render(request, 'account.html', context)

@login_required
def auth_admin(request):
	context = {}
	user = SiteUser.objects.get(email=request.user.email)
	if user.email != 'b.k.bolte@emory.edu': # Update admin authentication at some point
		return HttpResponseRedirect(reverse('index'))
	context['all_users'] = SiteUser.objects.all()
	return render(request, 'admin_home.html', context)
	

def admin_login(request):
	context_dict = {}
	return render_to_response('admin_login.html', context_dict)	
	
def admin_homepage(request):
	context_dict = {}
	return render_to_response('admin_homepage.html', context_dict)	
	 

def admin_browselist(request):
	context_dict = {}
		
	manuscripts = Manuscript.objects.all()

	if request.method == 'POST':
		#print len(non_final_manuscripts[0].reviewers.all())
		#print non_final_manuscripts[0].reviewers.all()[0].email
		
		# simple match based on keywords
		#for i in range(0, len(non_final_manuscripts)):
			# will be used in template
			#reviewrs = SiteUser.objects.filter(agreed_to_form=True, pi__in=non_final_manuscripts.keywords.split(','))
	
		# manuscripts with final decision being made
		#final_manuscripts = Manuscript.objects.filter(is_final=True)

		# use hidden value here to indicate which manuscript is being edited
		# AdminBrowseListForm(request.POST)

		print request.POST.getlist("reviewers")

	reviewers = SiteUser.objects.filter(agreed_to_form=True)
		
	context_dict['manuscripts'] = manuscripts
	return render_to_response('admin_browselist.html', context_dict, RequestContext(request))	
	
#def manuscript_detail(request):
#	context_dict = {}
#	return render(request, 'manuscript_detail.html', context_dict)
	
#def user_detail(request):
#	context_dict = {}
#	return render(request, 'user_detail.html', context_dict)	
	
def manuscript_detail(request, pk):
	manuscript = get_object_or_404(Manuscript, pk=pk)
	return render(request, 'manuscript_detail.html', {'manuscript': manuscript})
	
def user_detail(request, pk):
	user = get_object_or_404(SiteUser, pk=pk)
	return render(request, 'user_detail.html', {'user': user})
