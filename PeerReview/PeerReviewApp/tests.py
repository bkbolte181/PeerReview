from django.test import TestCase
from models import *
from django.utils import timezone
from forms import *
from django.test import Client
from django.utils import unittest
from django.core.urlresolvers import reverse
from forms import *


# Create your tests here.

class UserTest(TestCase):

    def create_user(self, email = 'johnny@emory.edu', password = '123', firstname = 'johnny', lastname= 'tan'):
        return SiteUser.objects.create(email = email, password = password, first_name = firstname, last_name = lastname)

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w,SiteUser))
        self.assertEqual(w.get_short_name(), 'johnny')
        self.assertEqual(w.get_full_name(),('johnny','tan'))

