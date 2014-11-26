from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404

from PeerReviewApp.models import *
from PeerReviewApp.forms import *

import json

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

def is_site_admin_check(user):
	if user.is_authenticated():
		return user.is_site_admin
	else:
		return False

def admin_login(request):
	#context_dict = {}
	context = {}
	#context['next'] = request.GET.get('next', False)
	if request.method == 'POST': form = AdminLoginForm(request.POST)
	else: form = AdminLoginForm()
	if form.is_valid() and 'email' in form.cleaned_data and 'password' in form.cleaned_data:
		print 'hit 2'

		user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
		print form.cleaned_data['email']
		print form.cleaned_data['password']
		print user
		if user is not None:
			print "hit 3"
			login(request, user)
			#if request.POST.get('next',False):
			#	return HttpResponseRedirect(request.POST.get('next', False))
			#else:
			print "hit 3"
			return HttpResponseRedirect(reverse('admin_homepage')) # Redirect to homepage when the user logs in
		else:
			context['errors'] = 'Authentication failed.'
	context['form'] = form
	#return render_to_response('login.html', context, context_instance=RequestContext(request))
	#return render_to_response('admin_login.html', context_dict)
	return render_to_response('admin_login.html', context, context_instance=RequestContext(request))

#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def admin_homepage(request):
	context_dict = {}
	period = ReviewPeriod.objects.filter(is_current=True)[0]
	print period
	submission_deadline = period.submission_deadline
	print submission_deadline
	review_deadline = period.review_deadline
	print review_deadline
	group_meeting_time = period.group_meeting_time
	print group_meeting_time
	group_meeting_venue = period.group_meeting_venue
	print group_meeting_venue
	context_dict['submission_deadline'] = submission_deadline
	context_dict['review_deadline'] = review_deadline
	context_dict['group_meeting_time'] = group_meeting_time
	context_dict['group_meeting_venue'] = group_meeting_venue
	#return render_to_response('admin_homepage.html', context_dict)
	return render_to_response('admin_homepage.html', context_dict, RequestContext(request))

class MatchedManuscript():
	manuscript = Manuscript
	
	def __init__(self):
		self.recommended_reviewers = []

	def add(self, reviewer):
		self.recommended_reviewers.append(reviewer)

#view to handle admin ajax call 
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def admin_ajax(request):
	try:
		if request.POST.has_key('manuscript_id'):
			manuscript_id = request.POST.get('manuscript_id')
			manuscript = Manuscript.objects.get(id=manuscript_id)

			#get new set of reviewers
			if request.POST.has_key('reviewers'):
				reviewers = request.POST.get('reviewers').split(',')
				reviewers.pop()

				#store the new set of reviewers
				manuscript.reviewers.clear()
				for reviewer in reviewers:
					manuscript.reviewers.add(SiteUser.objects.get(email=reviewer))
				response_dict = {}
				assigned_dict = {} 
				recommend_dict = {}
				
				#manuscript = Manuscript.objects.get(id=manuscript_id)
				#print manuscript.reviewers.all()[0].first_name

				for reviewer in manuscript.reviewers.all():
					assigned_dict[reviewer.email] = {'name':reviewer.first_name + ' ' + reviewer.last_name + reviewer.star_string, 'email':reviewer.email, 'id':reviewer.id, 'star':reviewer.star_string}
				for reviewer in manuscript.recommended_reviewers:
					recommend_dict[reviewer.email] = {'name':reviewer.first_name + ' ' + reviewer.last_name + reviewer.star_string, 'email':reviewer.email, 'id':reviewer.id, 'star':reviewer.star_string}
						
				response_dict['assigned'] = assigned_dict
				response_dict['recommend'] = recommend_dict

	except KeyError:
		return HttpResponse(json.dumps({'error': 'true', 'code': 'KeyError'}), content_type='application/json')

	return HttpResponse(json.dumps(response_dict), content_type='application/json')

#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def admin_browselist(request):
	context_dict = {}
		
	#period = ReviewPeriod.objects.all()[:1].get()
	period = ReviewPeriod.objects.filter(is_current=True)[0]
	print period
	submission_deadline = period.submission_deadline
	print submission_deadline
	review_deadline = period.review_deadline
	print review_deadline
	group_meeting_time = period.group_meeting_time
	print group_meeting_time
	group_meeting_venue = period.group_meeting_venue
	print group_meeting_venue

	#if request.method == 'POST':
		#finish editing
		#if request.POST.get("save") != None:
			#get the targeted manuscript
			#print "haha"
			#editing = Manuscript.objects.get(id=request.POST.get("save"));
			#editing.reviewers.clear()
			#for reviewer in request.POST.getlist("reviewers"):
				#editing.reviewers.add(SiteUser.objects.get(email=reviewer))
			
				#print SiteUser.objects.get(email=reviewer)
		#submit final decision
		#elif request.POST.get("final") != None:
		#	final = Manuscript.objects.get(id=request.POST.get("final"))
			#requset.POST.get(")
			#check constraint
			#while True:
			#	a = 1	
		#	final.is_final = True		
		#	final.save()
		
	manuscripts_all = Manuscript.objects.all()
	#print manuscripts[0].is_current
	#manuscripts = Manuscript.objects.filter(is_current=True)

	#review period constrain
	manuscripts = []
	for manuscript in manuscripts_all:
		if manuscript.review_period.is_current:
			manuscripts.append(manuscript)	

	#simple match, recommend reviewers
	reviewers = SiteUser.objects.filter(agreed_to_form=True)

	#context_dict['unfinished_manuscripts'] = matched_manuscripts
	#context_dict['final_manuscripts'] = final_manuscripts
	context_dict['manuscripts'] = manuscripts
	context_dict['reviewers'] = reviewers
	context_dict['submission_deadline'] = submission_deadline
	context_dict['review_deadline'] = review_deadline
	context_dict['group_meeting_time'] = group_meeting_time
	context_dict['group_meeting_venue'] = group_meeting_venue
	return render_to_response('admin_browselist.html', context_dict, RequestContext(request))	


#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def manuscript_detail(request, pk):
	manuscript = get_object_or_404(Manuscript, pk=pk)
	#return render(request, 'manuscript_detail.html', {'manuscript': manuscript})
	return render_to_response('manuscript_detail.html', {'manuscript': manuscript}, RequestContext(request))

#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def user_detail(request, pk):
	user = get_object_or_404(SiteUser, pk=pk)
	#return render(request, 'user_detail.html', {'user': user})
	return render_to_response('user_detail.html', {'user': user}, RequestContext(request))

#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def setting(request):
	if request.method == 'POST':
		form = ReviewPeriodForm(request.POST)
		if form.is_valid():
			for period in ReviewPeriod.objects.all():
				period.is_current = False
				period.save()
			#ReviewPeriod.objects.all().delete();
			period = form.save(commit=True)
			period.is_current = True
			period.save()
			for period in ReviewPeriod.objects.all():
				print period.is_current
			return render_to_response('setting_ok.html', {"period":period}, RequestContext(request))
		else:
			print form.errors
	else:
		form = ReviewPeriodForm()
	return render_to_response('setting.html', {'form': form}, RequestContext(request))

#@login_required(login_url='/admin_login')
@user_passes_test(is_site_admin_check, login_url='/admin_login')
def admin_logout(request):
	context = {}
	logout(request)
	return HttpResponseRedirect('/admin_login')
