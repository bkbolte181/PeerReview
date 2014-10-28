from django.test import TestCase
from models import *
from django.utils import timezone
from forms import *
from django.test import Client
from django.utils import unittest
from django.core.urlresolvers import reverse
from forms import *
import datetime


# Create your tests here.

class UserTest(TestCase):

    def create_user(self, email = 'johnny@emory.edu', password = '123', firstname = 'johnny', lastname= 'tan'):
        return SiteUser.objects.create(email = email, password = password, first_name = firstname, last_name = lastname)

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w,SiteUser))
        self.assertEqual(w.get_short_name(), 'johnny')
        self.assertEqual(w.get_full_name(),('johnny','tan'))


class ReviewPeriodTest(TestCase):

    def create_review_period(self, isfull = 'false', startdate = timezone.now(), submissionsdeadline = timezone.now()+ datetime.timedelta(days = 30), reviewdeadline = timezone.now()+datetime.timedelta(days = 50), groupmeeting = timezone.now()+datetime.timedelta(days = 80)):
        return ReviewPeriod.objects.create(is_full = isfull, start_date = startdate, submission_deadline = submissionsdeadline, review_deadline = reviewdeadline, group_meeting_time = groupmeeting )


    def test_review_period(self):
        r = self.create_review_period()
        self.assertTrue(isinstance(r,ReviewPeriod))
