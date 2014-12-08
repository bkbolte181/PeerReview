from django.test import TestCase
from django.utils import timezone
from django.test import Client
from django.utils import unittest
from django.core.urlresolvers import reverse
import datetime
from PeerReviewApp.models import *
from PeerReviewApp.forms import *
from PeerReviewApp.views import *

#PeerReviewApp.test.test_unit_tests
#test create user
class CreateUserTest(unittest.TestCase):

	def test_create_user(self):
		instance = SiteUser(email = 'johnny@emory.edu', password = '123'
		, first_name = 'johnny', last_name= 'tan')
		self.assertTrue(isinstance(instance, SiteUser))

#test get_short_name
class GetShortNameTest(unittest.TestCase):

	def test_get_short_name(self):
		instance = SiteUser(email = 'johnny@emory.edu', password = '123'
		, first_name = 'johnny', last_name= 'tan')
		self.assertEqual(instance.get_short_name(), 'johnny')

#test get_full_name
class GetFullNameTest(unittest.TestCase):

	def test_get_full_name(self):
		instance = SiteUser(email = 'johnny@emory.edu', password = '123'
		, first_name = 'johnny', last_name= 'tan')
		self.assertEqual(instance.get_full_name(), ('johnny','tan'))

#test get_star_string
class GetStarStringTest(unittest.TestCase):
	def test_get_star_string_true(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3)
		self.assertEqual(instance._get_star_string(), ('*'))
		
	def test_get_star_string_false(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 2)
		self.assertEqual(instance._get_star_string(), (''))

#test create review period
class CreateReviewPeriodTest(unittest.TestCase):

	def test_create_reviewperiod(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50))
		self.assertTrue(isinstance(instance, ReviewPeriod))

#test create manuscript 
class CreateManuscriptTest(unittest.TestCase):

	def test_create_manuscript(self):
		instance = Manuscript(status = 'submitted', abstract = 'abstract', title = 'title'
		, keywords = 'k1,k2,k3', is_final = 'False')
		self.assertTrue(isinstance(instance, Manuscript))

#class CreateReviewFileTest(unittest.TestCase):

#class CreateManuscriptFileTest(unittest.TestCase):

