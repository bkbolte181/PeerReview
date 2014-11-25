from django.test import TestCase
from django.utils import timezone
from django.test import Client
from django.utils import unittest
from django.core.urlresolvers import reverse
from django.db import transaction
import datetime
#import sys
#sys.path.append("..")

from PeerReviewApp.models import *
from PeerReviewApp.forms import *
from PeerReviewApp.views import *

class UserModelTest(TestCase):

	def test_user_model(self):
		#sid = transaction.savepoint()
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')

		''' test get '''
		get = SiteUser.objects.get(email='jhu39@emory.edu')
		self.assertEqual(instance.password, get.password)
		self.assertEqual(instance.first_name, get.first_name)
		self.assertEqual(instance.last_name, get.last_name)
		#transaction.savepoint_rollback(sid)

		''' test update '''
		self.assertFalse(get.agreed_to_form)
		get.agreed_to_form = True
		get.save()

		updated = SiteUser.objects.get(email='jhu39@emory.edu')
		self.assertTrue(updated.agreed_to_form)
		
class ReviewPeriodModelTest(TestCase):

	def test_reviewperiod_model(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50))
		self.assertTrue(isinstance(instance, ReviewPeriod)) 		
		instance.save()

		get = ReviewPeriod.objects.all()
		self.assertEqual(len(get),1)






