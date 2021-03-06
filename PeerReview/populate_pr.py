import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeerReview.settings')

import django
django.setup()

from PeerReviewApp.models import SiteUser, ReviewPeriod, Manuscript
import datetime

from django.contrib.auth import authenticate

def populate():
    admin_site_user = add_user(email='admin@gmail.com', password='123', agreed_to_form=False, is_site_admin=True)

    site_user1 = add_user(email='johnlee@emory.edu', password='123', first_name='John', last_name='Lee', department='Math & CS', school='Goizueta Business School', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
    site_user2 = add_user(email='marygreen@emory.edu', password='123', first_name='Mary', last_name='Green', department='Biostatistics', school='Laney Graduate School', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
    site_user3 = add_user(email='arial.m@emory.edu', password='123', first_name='Arial', last_name='Martinez', department='Business', school='School of Law', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Chemistry, Physics', review_count='4', agreed_to_form=True)
    site_user4 = add_user(email='rick.b@emory.edu', password='123', first_name='Rick', last_name='Buswell', department='Math & CS4', school='School of Law', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Physics, Mathematics', review_count='3', agreed_to_form=True)
    site_user5 = add_user(email='benb@emory.edu', password='123', first_name='Benjamin', last_name='Bolte', department='Math & CS5', school='Laney Graduate School', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Physics', review_count='11', agreed_to_form=True)
    site_user6 = add_user(email='emily.white@emory.edu', password='123', first_name='Emily', last_name='White', department='Math & CS', school='School of Law', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
    site_user7 = add_user(email='peng.ji@emory.edu', password='123', first_name='Peng', last_name='Ji', department='Biostatistics', school='School of Law', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
    site_user8 = add_user(email='jiulin.hu@emory.edu', password='123', first_name='Jiulin', last_name='Hu', department='Business', school='Nell Hodgson Woodruff School of Nursing', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, mathematics', review_count='4', agreed_to_form=True)
    site_user9 = add_user(email='johnny.tan@emory.edu', password='123', first_name='Johnny', last_name='Tan', department='Math & CS4', school='Laney Graduate School', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Finance', review_count='3', agreed_to_form=True)
    site_user10 = add_user(email='raul.doria@emory.edu', password='123', first_name='Raul', last_name='Doria', department='Math & CS5', school='Nell Hodgson Woodruff School of Nursing', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Industrial engineering, Machine learning', review_count='1', agreed_to_form=True)
    site_user11 = add_user(email='larry.villagrana@emory.edu', password='123', first_name='Larry', last_name='Villagrana', department='Math & CS', school='College of Arts and Sciences', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='3', agreed_to_form=True)
    site_user12 = add_user(email='cody.gagon@emory.edu', password='123', first_name='Cody', last_name='Gagnon', department='Biostatistics', school='Laney Graduate School', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
    site_user13 = add_user(email='zelma.clarkson@emory.edu', password='123', first_name='Zelma', last_name='Clarkson', department='Business', school='Nell Hodgson Woodruff School of Nursing', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, FINANCE', review_count='2', agreed_to_form=True)
    site_user14 = add_user(email='emily.green@emory.edu', password='123', first_name='Emily', last_name='Green', department='Math & CS4', school='Laney Graduate School', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
    site_user15 = add_user(email='emily.bourn@emory.edu', password='123', first_name='Emily', last_name='Bourn', department='Math & CS5', school='College of Arts and Sciences', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
    site_user16 = add_user(email='floretta@emory.edu', password='123', first_name='Floretta', last_name='Klingler', department='Math & CS', school='Nell Hodgson Woodruff School of Nursing', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='2', agreed_to_form=True)
    site_user17 = add_user(email='candra.bulger@emory.edu', password='123', first_name='Candra', last_name='Bulger', department='Biostatistics', school='Rollins School of Public Health', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
    site_user18 = add_user(email='sudie.benham@emory.edu', password='123', first_name='Sudie', last_name='Benham', department='Business', school='Rollins School of Public Health', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, Machine learning', review_count='1', agreed_to_form=True)
    site_user19 = add_user(email='jenna.geno@emory.edu', password='123', first_name='Jenna', last_name='Geno', department='Math & CS4', school='Rollins School of Public Health', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Machine learning', review_count='1', agreed_to_form=True)
    site_user20 = add_user(email='heide.woodley@emory.edu', password='123', first_name='Heide', last_name='Woodley', department='Math & CS5', school='College of Arts and Sciences', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Statistics, Machine learning', review_count='1', agreed_to_form=True)

    ReviewPeriod.objects.all().delete()
    period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=1, day=10), review_deadline=datetime.date(year=2015, month=2, day=10), group_meeting_time=datetime.date(year=2015, month=2, day=25), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.', is_current=True)

    Manuscript.objects.all().delete()
    manuscript4 = Manuscript.objects.get_or_create(keywords='math,Physics', title = 'LAD VS PDA5******', brief_title='LAD VS PDA4', abstract='ooooooo', review_period=period[0], field='Software Engineering', target_journal='target_journal', status="Submitted", is_final=True)
    manuscript4[0].reviewers.add(site_user2)
    manuscript4[0].reviewers.add(site_user10)
    manuscript4[0].reviewers.add(site_user16)
    manuscript4[0].authors.add(site_user6)

    manuscript1 = Manuscript.objects.get_or_create(keywords='lsa,bsa,tsa', title = 'PCA versus LDA PCA versus LDA PCA versus LDA', brief_title='PCA versus LDA', abstract='In the context of the appearance-based paradigm for object recognition, it is generally believed that algorithms based on LDA (Linear Discriminant Analysis) are superior to those based on PCA (Principal Components Analysis). In this communication, we show that this is not always the case. We present our case first by using intuitively plausible arguments and, then, by showing actual results on a face database. Our overall conclusion is that when the training data set is small, PCA can outperform LDA and, also, that PCA is less sensitive to different training data sets.', review_period=period[0], field='computer science', target_journal='IEEE Transaction on Machine Learning',status="Submitted",  is_final=False)
    manuscript1[0].reviewers.add(site_user1)
    manuscript1[0].reviewers.add(site_user19)
    manuscript1[0].authors.add(site_user3)

    manuscript2 = Manuscript.objects.get_or_create(keywords='math,eco', title = 'LAD VS PDA2******', brief_title='LAD VS PDA2', abstract='ooooooo', review_period=period[0], field='Mathematics', target_journal='target_journal', status="Submitted")
    manuscript2[0].reviewers.add(site_user2)
    manuscript2[0].reviewers.add(site_user4)
    manuscript2[0].reviewers.add(site_user16)
    manuscript2[0].authors.add(site_user4)

    manuscript3 = Manuscript.objects.get_or_create(keywords='math,Physics,finance', title = 'LAD VS PDA3*****',brief_title='LAD VS PDA3', abstract='ooooooo', review_period=period[0], field='Physics', target_journal='target_journal', status="Submitted")
    manuscript3[0].reviewers.add(site_user14)
    manuscript3[0].reviewers.add(site_user3)
    manuscript3[0].authors.add(site_user2)

    manuscript5 = Manuscript.objects.get_or_create(keywords='math,eco,finance', title = 'LAD VS PDA5*****',brief_title='LAD VS PDA5', abstract='ooooooo', review_period=period[0], field='Finance', target_journal='target_journal', is_final=True, status="Submitted")
    manuscript5[0].reviewers.add(site_user5)
    manuscript5[0].reviewers.add(site_user6)
    manuscript5[0].reviewers.add(site_user7)
    manuscript5[0].reviewers.add(site_user8)
    manuscript5[0].reviewers.add(site_user9)
    manuscript5[0].authors.add(site_user10)

    manuscript6 = Manuscript.objects.get_or_create(keywords='math,finance', title = 'LAD VS PDA6*****',brief_title='LAD VS PDA6', abstract='ooooooo', review_period=period[0], field='Finance', target_journal='target_journal', status="Submitted")
    manuscript6[0].authors.add(site_user15)

    return

def add_user(email, password, first_name="", last_name="", department="", school="", lab="", pi="", research_interest="", review_count="",
             agreed_to_form="", is_site_admin=False):
	if not SiteUser.objects.filter(email=email).count():
		site_user = SiteUser.objects.create_user(email=email, password=password)

	site_user=SiteUser.objects.filter(email=email)[0]
	site_user.first_name=first_name
	site_user.last_name=last_name
	site_user.department=department
	site_user.school=school
	site_user.lab=lab
	site_user.pi=pi
	site_user.research_interest=research_interest
	site_user.review_count=review_count
	site_user.agreed_to_form=agreed_to_form
	site_user.is_site_admin=is_site_admin
	site_user.save()
	user = authenticate(username=email, password=password)
	print user
	return site_user

if __name__ == '__main__':
    print "Starting PeerReview population script..."
    populate()
    print "done...."




















