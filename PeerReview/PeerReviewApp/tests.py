from django.test import TestCase
from models import *
from django.utils import timezone
from forms import *
from django.test import Client
from django.utils import unittest
from django.core.urlresolvers import reverse
from forms import *
from views import *
import datetime
import os

# Testing the Model

class UploadFilesTest(TestCase):
	""" Test file uploads """
	def create_user(self, email = 'johnny@emory.edu', password = '123', firstname = 'johnny', lastname= 'tan'):
		return SiteUser.objects.create(email = email, password = password, first_name = firstname, last_name = lastname)

	def create_review_period(self, isfull = 'false', startdate = timezone.now(), submissionsdeadline = timezone.now()+ datetime.timedelta(days = 30), reviewdeadline = timezone.now()+datetime.timedelta(days = 50), groupmeeting = timezone.now()+datetime.timedelta(days = 80)):
		return ReviewPeriod.objects.create(is_full = isfull, start_date = startdate, submission_deadline = submissionsdeadline, review_deadline = reviewdeadline, group_meeting_time = groupmeeting )

	def upload_image_file(self, file='anonymous.jpg'):
		usr = self.create_user()
		man = Manuscript.objects.create(status='submitted',
										title='A Silly Title: A Treatise on Modern Titles in America and the Silliness Therein',
										brief_title='A Silly Title',
										abstract='Abstract? What abstract?',
										keywords='f**k,s**t,m****rf****r', # Censored for the children
										field='Silliness',
										target_journal='Silly Journal',
										review_period=self.create_review_period(),
										is_final=False)
		return ImageFile.objects.create(file=os.path.join(settings.MEDIA_ROOT, file), manuscript=man)

	def test_file_upload(self):
		img = self.upload_image_file()
		self.assertTrue(isinstance(img,ImageFile))
		self.assertTrue(os.path.isfile(img.file.path))

class CreateUserTest(TestCase):

    def create_user(self, email = 'johnny@emory.edu', password = '123', firstname = 'johnny', lastname= 'tan'):
        return SiteUser.objects.create(email = email, password = password, first_name = firstname, last_name = lastname)

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w,SiteUser))
        self.assertEqual(w.get_short_name(), 'johnny')
        self.assertEqual(w.get_full_name(),('johnny','tan'))


class CreateReviewPeriodTest(TestCase):

    def create_review_period(self, isfull = 'false', startdate = timezone.now(), submissionsdeadline = timezone.now()+ datetime.timedelta(days = 30), reviewdeadline = timezone.now()+datetime.timedelta(days = 50), groupmeeting = timezone.now()+datetime.timedelta(days = 80)):
        return ReviewPeriod.objects.create(is_full = isfull, start_date = startdate, submission_deadline = submissionsdeadline, review_deadline = reviewdeadline, group_meeting_time = groupmeeting )


    def test_review_period(self):
        r = self.create_review_period()
        self.assertTrue(isinstance(r,ReviewPeriod))


# class CreateManuscriptModelTest(TestCase):


# Testing the Views
# For status_code 302 is redirect urls, 200 is normal resp status code , 301 is permanently moved links


class SignupView(TestCase):

    def test_signup(self):
        resp = self.client.get('/signup/')
        self.assertEquals(resp.status_code,200)

class AdminView(TestCase):

    def test_admin(self):
        resp = self.client.get('/admin/')
        self.assertEquals(resp.status_code,302)

class TermsView(TestCase):

    def test_term(self):
        resp = self.client.get('/terms/')
        self.assertEqual(resp.status_code,200)

class LoginView(TestCase):

    def test_login(self):
        resp = self.client.get('/login/')
        self.assertEquals(resp.status_code,200)

class AccountView(TestCase):

    def test_account(self):
        resp = self.client.get('/account/')
        self.assertEquals(resp.status_code,302)

class LogoutView(TestCase):

    def test_logout(self):
        resp = self.client.get('/logout/')
        self.assertEquals(resp.status_code,302)

'''
class UploadView(TestCase):

    def test_upload(self):
        resp = self.client.get('/upload')
        self.assertEquals(resp.status_code,301)
'''

class ReviewView(TestCase):

    def test_review(self):
        resp = self.client.get('/review/')
        self.assertEquals(resp.status_code,302)

class BrowseView(TestCase):

    def test_browse(self):
        resp = self.client.get('/browse/1')
        self.assertEquals(resp.status_code,301)
        #self.assertTrue('all_manuscript' in resp.content)

class AssignedManuscriptView(TestCase):

    def test_assigned(self):
        resp = self.client.get('/assignedmanuscripts/')
        self.assertEquals(resp.status_code,302)

class AgreementView(TestCase):

    def test_agreement(self):
        resp = self.client.get('/agreement/')
        self.assertEquals(resp.status_code,302)


# Form testing






