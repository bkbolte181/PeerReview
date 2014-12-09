from django.utils import unittest
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.db import transaction
from django.core.urlresolvers import reverse

from PeerReviewApp.models import *
from PeerReviewApp.forms import *
from PeerReviewApp.views import *

import datetime

#test the operations of SiteUser model
class UserModelTest(TestCase):

	#test get instance
	def test_user_model_get_user(self):
		#sid = transaction.savepoint()
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')

		get = SiteUser.objects.get(email='jhu39@emory.edu')

		self.assertEqual(instance.password, get.password)
		self.assertEqual(instance.first_name, get.first_name)
		self.assertEqual(instance.last_name, get.last_name)
		#transaction.savepoint_rollback(sid)

	#test update 
	def test_user_model_update_user(self):
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')

		get = SiteUser.objects.get(email='jhu39@emory.edu')

		self.assertFalse(get.agreed_to_form)
		get.agreed_to_form = True
		get.save()

	#test register with exist email		
	def test_user_model_register_with_exist_email(self):
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')	

		#instance1 = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		#, first_name='Jiulin', last_name='Hu')

		#updated = SiteUser.objects.get(email='jhu39@emory.edu')
		#self.assertTrue(updated.agreed_to_form)

	#test delete user
	def test_user_model_delete_user(self):
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')	

		get = SiteUser.objects.all()
		self.assertEqual(len(get), 1)
	
		instance.delete()
				
		get = SiteUser.objects.all()
		self.assertEqual(len(get), 0)

	#test delete a list of users
	def test_user_model_delete_user_list(self):
		instance1 = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')	
		instance2 = SiteUser.objects.create(email='jhu38@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')	
		instance2 = SiteUser.objects.create(email='jhu37@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')			

		get = SiteUser.objects.all()
		self.assertEqual(len(get), 3)

		SiteUser.objects.all().delete()
		
		get = SiteUser.objects.all()
		self.assertEqual(len(get), 0)

	#test assign manuscript to user
	def test_user_model_assign_manuscript(self):
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')			

		period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=1, day=10), review_deadline=datetime.date(year=2015, month=2, day=10), group_meeting_time=datetime.date(year=2015, month=2, day=25), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.', is_current=True)
		
		manuscript1 = Manuscript.objects.get_or_create(keywords='math,Physics', title = 'LAD VS PDA5******', brief_title='LAD VS PDA4', abstract='ooooooo', review_period=period[0], field='Software Engineering', target_journal='target_journal', is_final=True)
		instance.reviewers.add(manuscript1[0])
		#self.assertEqual(instance.reviewers.all()[0], manuscript1)		
		self.assertEqual(1, len(instance.reviewers.all()))		
		self.assertEqual(instance.reviewers.all()[0].id, manuscript1[0].id)

	#test get assigned manuscript number of a user
	def test_user_model_assigned_num(self):
		instance = SiteUser.objects.create(email='jhu39@emory.edu', password='123'
		, first_name='Jiulin', last_name='Hu')			

		period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=1, day=10), review_deadline=datetime.date(year=2015, month=2, day=10), group_meeting_time=datetime.date(year=2015, month=2, day=25), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.', is_current=True)
		
		manuscript1 = Manuscript.objects.get_or_create(keywords='math,Physics', title = 'LAD VS PDA5******', brief_title='LAD VS PDA4', abstract='ooooooo', review_period=period[0], field='Software Engineering', target_journal='target_journal', is_final=True)

		manuscript2 = Manuscript.objects.get_or_create(keywords='lsa,bsa,tsa', title = 'PCA versus LDA PCA versus LDA PCA versus LDA', brief_title='PCA versus LDA', abstract='In the context of the appearance-based paradigm for object recognition, it is generally believed that algorithms based on LDA (Linear Discriminant Analysis) are superior to those based on PCA (Principal Components Analysis). In this communication, we show that this is not always the case. We present our case first by using intuitively plausible arguments and, then, by showing actual results on a face database. Our overall conclusion is that when the training data set is small, PCA can outperform LDA and, also, that PCA is less sensitive to different training data sets.', review_period=period[0], field='computer science', target_journal='IEEE Transaction on Machine Learning', is_final=False)

		instance.reviewers.add(manuscript1[0])
		instance.reviewers.add(manuscript2[0])
		self.assertEqual(instance.assigned_num, 2)		


class ReviewPeriodModelTest(TestCase):

	#test get review period
	def test_reviewperiod_get(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50))
		self.assertTrue(isinstance(instance, ReviewPeriod)) 		
		instance.save()

		get = ReviewPeriod.objects.all()
		self.assertEqual(len(get),1)

	#test update review period
	def test_reviewperiod_update(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50)
		, is_current=True)
		instance.save()

		get = ReviewPeriod.objects.all()[0]
		get.is_current = False
		get.save()
	
		self.assertEqual(ReviewPeriod.objects.all()[0].is_current, False)

	#test delete review period
	def test_reviewperiod_delete(self):
		instance = ReviewPeriod(is_full = 'False', start_date = timezone.now()
		, submission_deadline = timezone.now()
		, review_deadline = timezone.now()+datetime.timedelta(days = 30)
		, group_meeting_time = timezone.now()+datetime.timedelta(days = 50)
		, is_current=True)
		instance.save()		

		get = ReviewPeriod.objects.all()[0]
		get.delete()
		get = ReviewPeriod.objects.all()
		
		self.assertEqual(len(get), 0)

class ManuscriptModelTest(TestCase):
	def add_user(self, email, password, first_name="", last_name="", department="", lab="", pi="", research_interest="", review_count="",
             agreed_to_form="", is_site_admin=False):
	    if not SiteUser.objects.filter(email=email).count():
	        site_user = SiteUser.objects.create_user(email=email, password=password)
	
	    site_user=SiteUser.objects.filter(email=email)[0]
	    site_user.first_name=first_name
	    site_user.last_name=last_name
	    site_user.department=department
	    site_user.lab=lab
	    site_user.pi=pi
	    site_user.research_interest=research_interest
	    site_user.review_count=review_count
	    site_user.agreed_to_form=agreed_to_form
	    site_user.is_site_admin=is_site_admin
	    site_user.save()
	    #user = authenticate(username=email, password=password)

	#test manuscript get
	def test_manuscript_get(self):
		admin_site_user = self.add_user(email='admin@gmail.com', password='123', agreed_to_form=False, is_site_admin=True)

		site_user1 = self.add_user(email='johnlee@emory.edu', password='123', first_name='John', last_name='Lee', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
		site_user2 = self.add_user(email='marygreen@emory.edu', password='123', first_name='Mary', last_name='Green', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
		site_user3 = self.add_user(email='arial.m@emory.edu', password='123', first_name='Arial', last_name='Martinez', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Chemistry, Physics', review_count='4', agreed_to_form=True)
		site_user4 = self.add_user(email='rick.b@emory.edu', password='123', first_name='Rick', last_name='Buswell', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Physics, Mathematics', review_count='3', agreed_to_form=True)
		site_user5 = self.add_user(email='benb@emory.edu', password='123', first_name='Benjamin', last_name='Bolte', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Physics', review_count='11', agreed_to_form=True)
		site_user6 = self.add_user(email='emily.white@emory.edu', password='123', first_name='Emily', last_name='White', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
		site_user7 = self.add_user(email='peng.ji@emory.edu', password='123', first_name='Peng', last_name='Ji', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
		site_user8 = self.add_user(email='jiulin.hu@emory.edu', password='123', first_name='Jiulin', last_name='Hu', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, mathematics', review_count='4', agreed_to_form=True)
		site_user9 = self.add_user(email='johnny.tan@emory.edu', password='123', first_name='Johnny', last_name='Tan', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Finance', review_count='3', agreed_to_form=True)
		site_user10 = self.add_user(email='raul.doria@emory.edu', password='123', first_name='Raul', last_name='Doria', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Industrial engineering, Machine learning', review_count='1', agreed_to_form=True)
		site_user11 = self.add_user(email='larry.villagrana@emory.edu', password='123', first_name='Larry', last_name='Villagrana', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='3', agreed_to_form=True)
		site_user12 = self.add_user(email='cody.gagon@emory.edu', password='123', first_name='Cody', last_name='Gagnon', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
		site_user13 = self.add_user(email='zelma.clarkson@emory.edu', password='123', first_name='Zelma', last_name='Clarkson', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, FINANCE', review_count='2', agreed_to_form=True)
		site_user14 = self.add_user(email='emily.green@emory.edu', password='123', first_name='Emily', last_name='Green', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
		site_user15 = self.add_user(email='emily.bourn@emory.edu', password='123', first_name='Emily', last_name='Bourn', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
		site_user16 = self.add_user(email='floretta@emory.edu', password='123', first_name='Floretta', last_name='Klingler', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='2', agreed_to_form=True)
		site_user17 = self.add_user(email='candra.bulger@emory.edu', password='123', first_name='Candra', last_name='Bulger', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
		site_user18 = self.add_user(email='sudie.benham@emory.edu', password='123', first_name='Sudie', last_name='Benham', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, Machine learning', review_count='1', agreed_to_form=True)
		site_user19 = self.add_user(email='jenna.geno@emory.edu', password='123', first_name='Jenna', last_name='Geno', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Machine learning', review_count='1', agreed_to_form=True)
		site_user20 = self.add_user(email='heide.woodley@emory.edu', password='123', first_name='Heide', last_name='Woodley', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Statistics, Machine learning', review_count='1', agreed_to_form=True)

		period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=1, day=10), review_deadline=datetime.date(year=2015, month=2, day=10), group_meeting_time=datetime.date(year=2015, month=2, day=25), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.', is_current=True)

		manuscript4 = Manuscript.objects.get_or_create(keywords='math,Physics', title = 'LAD VS PDA5******', brief_title='LAD VS PDA4', abstract='ooooooo', review_period=period[0], field='Software Engineering', target_journal='target_journal', is_final=True)
		#manuscript4[0].reviewers.add(site_user2)
		#manuscript4[0].reviewers.add(site_user10)
		#manuscript4[0].reviewers.add(site_user16)
		#manuscript4[0].authors.add(site_user6)

		manuscript1 = Manuscript.objects.get_or_create(keywords='lsa,bsa,tsa', title = 'PCA versus LDA PCA versus LDA PCA versus LDA', brief_title='PCA versus LDA', abstract='In the context of the appearance-based paradigm for object recognition, it is generally believed that algorithms based on LDA (Linear Discriminant Analysis) are superior to those based on PCA (Principal Components Analysis). In this communication, we show that this is not always the case. We present our case first by using intuitively plausible arguments and, then, by showing actual results on a face database. Our overall conclusion is that when the training data set is small, PCA can outperform LDA and, also, that PCA is less sensitive to different training data sets.', review_period=period[0], field='computer science', target_journal='IEEE Transaction on Machine Learning', is_final=False)
		#manuscript1[0].reviewers.add(site_user1)
		#manuscript1[0].reviewers.add(site_user19)
		#manuscript1[0].authors.add(site_user3)

		manuscript2 = Manuscript.objects.get_or_create(keywords='math,eco', title = 'LAD VS PDA2******', brief_title='LAD VS PDA2', abstract='ooooooo', review_period=period[0], field='Mathematics', target_journal='target_journal')
		#manuscript2[0].reviewers.add(site_user2)
		#manuscript2[0].reviewers.add(site_user4)
		#manuscript2[0].reviewers.add(site_user16)
		#manuscript2[0].authors.add(site_user4)

		manuscript3 = Manuscript.objects.get_or_create(keywords='math,Physics,finance', title = 'LAD VS PDA3*****',brief_title='LAD VS PDA3', abstract='ooooooo', review_period=period[0], field='Physics', target_journal='target_journal')
		#manuscript3[0].reviewers.add(site_user14)
		#manuscript3[0].reviewers.add(site_user3)
		#manuscript3[0].authors.add(site_user2)

		manuscript5 = Manuscript.objects.get_or_create(keywords='math,eco,finance', title = 'LAD VS PDA5*****',brief_title='LAD VS PDA5', abstract='ooooooo', review_period=period[0], field='Finance', target_journal='target_journal', is_final=True)
		#manuscript5[0].reviewers.add(site_user5)
		#manuscript5[0].reviewers.add(site_user6)
		#manuscript5[0].reviewers.add(site_user7)
		#manuscript5[0].reviewers.add(site_user8)
		#manuscript5[0].reviewers.add(site_user9)
		#manuscript5[0].authors.add(site_user10)

		manuscript6 = Manuscript.objects.get_or_create(keywords='math,finance', title = 'LAD VS PDA6*****',brief_title='LAD VS PDA6', abstract='ooooooo', review_period=period[0], field='Finance', target_journal='target_journal')
		#manuscript6[0].authors.add(site_user15)





