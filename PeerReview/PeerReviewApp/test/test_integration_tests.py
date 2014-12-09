from django.utils import unittest
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import datetime

class IntegrationTest(TestCase):

	def test_redirect(self):
		c = Client()

		#response = c.get('/login/', follow = True)
		#self.assertEquals(response.status_code,200)

		# Test if logout is a redirect
		#response = c.get('/logout/',follow = True)
		#self.assertRedirects(response,'http://testserver/login/?next=/logout/'
		#, status_code=302,target_status_code = 200, msg_prefix ='')

		#response = c.get('/signup/')
		#self.assertEquals(response.status_code, 200)

		#response = c.post('/login/?next=/agreement/') 
		#self.assertEquals(response.status_code, 200)

		#response = c.get('/login/?next=/agreement/')
		#self.assertRedirects(response,'/agreement/', status_code=302, target_status_code = 200, msg_prefix = '')

		#response = c.get('/login/?next=/account/', follow = True)
		#self.assertRedirects(response,'/account/', status_code = 302, target_status_code = 200, msg_prefix = '')

        # Reviewer Redirect Test
		#response = c.get('/agreement/?next=/review/', follow = True)
		#self.assertRedirects(response,'/review/', status_code = 302, target_status_code = 200, msg_prefix = '')
		
		#response = c.get('/login/?next=/agreement/%3Fnext%3D%252Freview%252F',follow = True)
		#self.assertRedirects(response,'/review/',status_code = 302, target_status_code = 200, msg_prefix = '')

		#response = c.get('/login/?next=/account/', follow = True)
		#self.assertRedirects(response,'/account/', status_code = 302, target_status_code = 200, msg_prefix = '')


class SignupViewTest(TestCase):
	def test_signup(self):
		resp = self.client.get('/signup/')
		self.assertEquals(resp.status_code,200)
		#self.assertTrue('form' in resp.context)

	#def test_post(self):
		#resp = self.client.post('/signup/', {'email':'123@emory.edu', 'first_name':'Jiulin','last_name':'Hu','department':'cs', 'lab':'cs', 'pi':'tt', 'school':'Goizueta Business School', 'Review_Count':'4', 'password':'123', 'retype_password':'456'})
		#self.assertTrue('errors' in resp.context)
		#print resp.context[1]
		#self.assertEqual(resp.context['errors'], 'The passwords you entered do not match.')


class AdminViewTest(TestCase):
	
    def test_admin(self):
        resp = self.client.get('/admin/')
        self.assertEquals(resp.status_code,302)

class TermsViewTest(TestCase):

    def test_term(self):
        resp = self.client.get('/terms/')
        self.assertEqual(resp.status_code,200)

class LoginViewTest(TestCase):

    def test_login(self):
        resp = self.client.get('/login/')
        self.assertEquals(resp.status_code,200)

#class AccountViewTest(TestCase):

#    def test_account(self):
#        resp = self.client.get('/account/')
#        self.assertEquals(resp.status_code,302)

class LogoutViewTest(TestCase):

    def test_logout(self):
        resp = self.client.get('/logout/')
        self.assertEquals(resp.status_code,302)

class UploadViewTest(TestCase):

    def test_upload(self):
        resp = self.client.get('/uploadmanuscript/')
        self.assertEquals(resp.status_code,302)

class ReviewViewTest(TestCase):

    def test_review(self):
        resp = self.client.get('/review/')
        self.assertEquals(resp.status_code,302)

class BrowseViewTest(TestCase):

    def test_browse(self):
        resp = self.client.get('/browse/1')
        self.assertEquals(resp.status_code,301)
        #self.assertTrue('all_manuscript' in resp.content)

class AssignedManuscriptViewTest(TestCase):

    def test_assigned(self):
        resp = self.client.get('/assignedmanuscripts/1')
        self.assertEquals(resp.status_code,301)

class AgreementViewTest(TestCase):

    def test_agreement(self):
        resp = self.client.get('/agreement/')
        self.assertEquals(resp.status_code,302)


