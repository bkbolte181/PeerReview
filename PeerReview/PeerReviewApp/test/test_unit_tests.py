from django.utils import unittest
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from PeerReviewApp.models import *
from PeerReviewApp.forms import *
from PeerReviewApp.views import *

import datetime

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

#test is_normal_user_ 
class IsNormalUserTest(unittest.TestCase):
	
	def test_is_normal_user_true(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = False)
		self.assertEqual(is_normal_user_(instance), True)

	def test_is_normal_user_false(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = True)
		self.assertEqual(is_normal_user_(instance), False)

#test is_normal_user_check
class IsAuthenticatedNormalUserTest(unittest.TestCase):
	
	def test_is_normal_user_check_true(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = False)
		self.assertEqual(is_normal_user_check(instance), True)

	def test_is_normal_user_check_false(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = True)
		self.assertEqual(is_normal_user_check(instance), False)

#test is_site_admin_check
class IsAuthenticatedAdminTest(unittest.TestCase):
	
	def test_is_site_admin_check_true(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = True)
		self.assertEqual(is_site_admin_check(instance), True)

	def test_is_site_admin_check_false(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = False)
		self.assertEqual(is_site_admin_check(instance), False)

#test has_agreed
class HasAgreedTest(unittest.TestCase):

	def test_has_agreed_admin(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = True)
		self.assertEqual(has_agreed(instance), False)

	def test_has_agreed_true(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = False, agreed_to_form = True)
		self.assertEqual(is_normal_user_check(instance), True)

	def test_has_agreed_false(self):
		instance = SiteUser(email = 'jiulin@emory.edu', password = '123'
		, review_count = 3, is_site_admin = True, agreed_to_form = False)
		self.assertEqual(is_normal_user_check(instance), False)

#test create review period
class CreateReviewPeriodTest(unittest.TestCase):

	def test_create_reviewperiod(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50))
		self.assertTrue(isinstance(instance, ReviewPeriod))

#test get current review period
#class GetCurrentReviewPeriodTest(unittest.TestCase):

#	def test_get_current_review_period():
#		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
#		, submission_deadline = timezone.now()
#		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
#		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50)
#		, is_current = True)		

#test create manuscript 
class CreateManuscriptTest(unittest.TestCase):

	def test_create_manuscript(self):
		instance = Manuscript(status = 'submitted', abstract = 'abstract', title = 'title'
		, keywords = 'k1,k2,k3', is_final = 'False')
		self.assertTrue(isinstance(instance, Manuscript))

#class CreateReviewFileTest(unittest.TestCase):

#class CreateManuscriptFileTest(unittest.TestCase):

