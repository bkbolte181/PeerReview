from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict
from datetime import date
from datetime import datetime
from filetransfers.api import prepare_upload
from forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PeerReviewApp.models import *
from PeerReviewApp.forms import *
from uuid import uuid4
import json


def handle_reviewer_uploads(request):
    ''' Method for dealing with the reviewer's uploaded review document '''
    upload_dir = date.today().strftime(settings.REVIEW_DOC_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    # Get  first uploaded file
    upload = request.FILES.getlist('file')[0]

    ext = upload.name.split('.')[-1]

    fname = str(uuid4()) + ext
    dest = open(os.path.join(upload_full_path, fname), 'wb')

    for chunk in upload.chunks():
        dest.write(chunk)
    dest.close()
    return (upload.name, os.path.join(upload_dir, fname))


def handle_uploads(request):
    ''' Method for dealing with uploaded files '''
    saved = []
    upload_dir = date.today().strftime(settings.UPLOAD_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    for upload in request.FILES.getlist('file'):
        # Ensure file uploads are unique
        ext = upload.name.split('.')[-1]
        fname = str(uuid4()) + ext
        dest = open(os.path.join(upload_full_path, fname), 'wb')
        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()
        saved.append((upload.name, os.path.join(upload_dir, fname)))
    return saved


def get_current_review_period():
    if ReviewPeriod.objects.count() > 0:
        return ReviewPeriod.objects.first()
    else:
        return False


def index(request):
    ''' Main landing page '''
    context = {}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {})


def terms(request):
    ''' Terms of service agreement '''
    context = {}
    return render(request, 'terms.html', context)


def auth_login(request):
    context = {}
    context['next'] = request.GET.get('next', False)
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    if form.is_valid() and 'email' in form.cleaned_data and 'password' in form.cleaned_data:
        print 'hit 2'
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            if request.POST.get('next', False):
                return HttpResponseRedirect(request.POST.get('next', False))
            else:
                return HttpResponseRedirect(reverse('index'))  # Redirect to homepage when the user logs in
        else:
            context['errors'] = 'Authentication failed.'
    context['form'] = form
    return render_to_response('login.html', context, context_instance=RequestContext(request))


def signup(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
    else:
        form = SignupForm()
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
        login(request, user)  # Log the user in
        return HttpResponseRedirect(reverse('index'))  # Redirect them to the home page
    context['form'] = form
    return render(request, 'signup.html', context)


@login_required
def agreement(request):
    ''' Agree to the form '''
    context = {}
    user = SiteUser.objects.get(email=request.user.email)
    if request.GET.get('next', False):
        next = request.GET.get('next', False)
        context['next'] = next
    elif request.POST.get('next', False):
        next = request.POST.get('next', False)
        context['next'] = next
    else:
        next = reverse('index')
    if request.POST:
        form = AgreementForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(next)
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
    context['period'] = get_current_review_period()
    return render(request, 'reviewer_home.html', context)


@user_passes_test(has_agreed, login_url='/agreement/')
def remove_associated_file(request, fid):
    print 'hit this'
    if request.is_ajax():
        context = {}
        f = ManuscriptFile.objects.get(id=fid)
        f.delete()
        context['msg'] = 'Deleted manuscript file'
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return Http404


@user_passes_test(has_agreed, login_url='/agreement/')
def submit_manuscript(request, mid):
    context = {}
    manuscript = Manuscript.objects.get(id=mid)
    manuscript.is_final = True
    manuscript.status = 'Submitted'
    manuscript.save()
    context['manuscript'] = manuscript
    return render(request, 'submit_manuscript.html', context)

@user_passes_test(has_agreed, login_url='/agreement/')
def delete_manuscript(request,mid):
    context = {}
    manuscript = Manuscript.objects.get(id=mid)
    manuscript.delete()
    manuscript.save()
    context['manuscript'] = manuscript
    return render(request, 'delete_manuscript.html', context)


@user_passes_test(has_agreed, login_url='/agreement/')
def edit_manuscript(request, mid):
	context = {}

	# If the user has made changes
	if 'submitbutton' in request.POST:
		# Need to write method to update form and associated files
		man = Manuscript.objects.get(id=request.POST['id'])
		form = UploadManuscript(request.POST, instance=man)
		if form.is_valid():
			form.save()

		saved_files = handle_uploads(request)
		for f in saved_files:
			m = ManuscriptFile.objects.create(filename=f[0], upload=f[1], manuscript=man)
			m.save()
		return render(request,'uploader_home.html')
	else:

		#Get the current user and the manuscript being edited
		user = SiteUser.objects.get(email=request.user.email)
		manuscript = Manuscript.objects.get(id=mid)

		# Make sure the manuscript they're trying to edit is theirs and that it can be edited
		if user not in manuscript.authors.all():
		    context['error'] = 'You are not authorized to make changes to this manuscript.'
		    return render(request, 'edit_manuscript.html', context)
		elif manuscript.is_final:
		    context['error'] = 'This manuscript can no longer be edited.'
		    return render(request, 'edit_manuscript.html', context)

		form = UploadManuscript(instance=manuscript)
		context['form'] = form

		files = ManuscriptFile.objects.filter(manuscript=manuscript)
		context['files'] = files

		context['manuscript'] = manuscript

		return render(request, 'edit_manuscript.html', context)


@user_passes_test(has_agreed, login_url='/agreement/')
def browse_manuscripts(request, current_page):
    context = {}
    context['period'] = get_current_review_period()
    # Load all available manuscripts
    all_manuscripts = Manuscript.objects.all()

    # Create a paginator with the manuscripts
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
def assigned_manuscripts(request, current_page):
    context = {}
    context['period'] = get_current_review_period()

    # Load the current user and get the manuscripts for which they are a reviewer
    user = SiteUser.objects.get(email=request.user.email)
    manuscripts_assigned = Manuscript.objects.filter(reviewers__in=[user]).all()

    if request.FILES:
        mid = request.POST.get('manid')
        man = Manuscript.objects.get(id=mid)
        saved_file = handle_reviewer_uploads(request)
        r = ReviewFile.objects.create(filename=saved_file[0], upload=saved_file[1], manuscript=man)
        r.save()
        man.reviewdocs = [r]
        man.save()

    # Create a paginator
    paginator = Paginator(manuscripts_assigned, 10)

    try:
        page = paginator.page(current_page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context['page'] = page
    return render(request, 'assigned_manuscripts.html', context)


@user_passes_test(has_agreed, login_url='/agreement/')
def author_home(request):
    context = {}
    context['period'] = get_current_review_period()
    return render(request, 'uploader_home.html', context)


@user_passes_test(has_agreed, login_url='/agreement/')
def upload_manuscript(request):
    context = {}
    context['period'] = get_current_review_period()
    if request.POST:
        form = UploadManuscript(request.POST)

        if form.is_valid():
            man = form.save()

            # Set current user as author
            current_user = SiteUser.objects.get(email=request.user.email)
            man.authors = [current_user]

            saved_files = handle_uploads(request)
            for f in saved_files:
                m = ManuscriptFile.objects.create(filename=f[0], upload=f[1], manuscript=man)
                m.save()

            # If successful, redirect to main page
            return HttpResponseRedirect(reverse('authorhome'))
    else:
        form = UploadManuscript()
    context['form'] = form
    return render(request, 'upload_manuscript.html', context)


@login_required
def account(request):
    context = {}
    user = SiteUser.objects.get(email=request.user.email)
    if 'delete' in request.POST:
        print 'Deleting account ' + str(user)
        logout(request)
        user.delete()
        return HttpResponseRedirect(reverse('index'))
    if 'savebutton' in request.POST:
        form = AccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            context['errors'] = 'Information saved.'
        return HttpResponseRedirect(reverse('index'))
    else:
        form = AccountForm(instance=user)
    context['form'] = form
    return render(request, 'account.html', context)


@login_required
def auth_admin(request):
    context = {}
    user = SiteUser.objects.get(email=request.user.email)
    if user.email != 'b.k.bolte@emory.edu':  # Update admin authentication at some point
        return HttpResponseRedirect(reverse('index'))
    context['all_users'] = SiteUser.objects.all()
    return render(request, 'admin_home.html', context)
