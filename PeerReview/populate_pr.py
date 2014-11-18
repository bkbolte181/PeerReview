import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeerReview.settings')

import django
django.setup()

from PeerReviewApp.models import SiteUser, ReviewPeriod, Manuscript
import datetime

def populate():
    #SiteUser.objects.filter(agreed_to_form=True).delete()

    site_user1 = SiteUser.objects.get_or_create(email='johnlee@emory.edu', password='123', first_name='John', last_name='Lee', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
    site_user2 = SiteUser.objects.get_or_create(email='marygreen@emory.edu', password='123', first_name='Mary', last_name='Green', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
    site_user3 = SiteUser.objects.get_or_create(email='arial.m@emory.edu', password='123', first_name='Arial', last_name='Martinez', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Chemistry, Physics', review_count='4', agreed_to_form=True)
    site_user4 = SiteUser.objects.get_or_create(email='rick.b@emory.edu', password='123', first_name='Rick', last_name='Buswell', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Physics, Mathematics', review_count='3', agreed_to_form=True)
    site_user5 = SiteUser.objects.get_or_create(email='benb@emory.edu', password='123', first_name='Benjamin', last_name='Bolte', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Physics', review_count='11', agreed_to_form=True)
    site_user6 = SiteUser.objects.get_or_create(email='emily.white@emory.edu', password='123', first_name='Emily', last_name='White', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='5', agreed_to_form=True)
    site_user7 = SiteUser.objects.get_or_create(email='peng.ji@emory.edu', password='123', first_name='Peng', last_name='Ji', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='4', agreed_to_form=True)
    site_user8 = SiteUser.objects.get_or_create(email='jiulin.hu@emory.edu', password='123', first_name='Jiulin', last_name='Hu', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, mathematics', review_count='4', agreed_to_form=True)
    site_user9 = SiteUser.objects.get_or_create(email='johnny.tan@emory.edu', password='123', first_name='Johnny', last_name='Tan', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Finance', review_count='3', agreed_to_form=True)
    site_user10 = SiteUser.objects.get_or_create(email='raul.doria@emory.edu', password='123', first_name='Raul', last_name='Doria', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Industrial engineering, Machine learning', review_count='1', agreed_to_form=True)
    site_user11 = SiteUser.objects.get_or_create(email='larry.villagrana@emory.edu', password='123', first_name='Larry', last_name='Villagrana', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='3', agreed_to_form=True)
    site_user12 = SiteUser.objects.get_or_create(email='cody.gagon@emory.edu', password='123', first_name='Cody', last_name='Gagnon', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
    site_user13 = SiteUser.objects.get_or_create(email='zelma.clarkson@emory.edu', password='123', first_name='Zelma', last_name='Clarkson', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, FINANCE', review_count='2', agreed_to_form=True)
    site_user14 = SiteUser.objects.get_or_create(email='emily.green@emory.edu', password='123', first_name='Emily', last_name='Green', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
    site_user15 = SiteUser.objects.get_or_create(email='emily.bourn@emory.edu', password='123', first_name='Emily', last_name='Bourn', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Software Engineering, Mathematics', review_count='1', agreed_to_form=True)
    site_user16 = SiteUser.objects.get_or_create(email='floretta@emory.edu', password='123', first_name='Floretta', last_name='Klingler', department='Math & CS', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest='Computer science, Software Engineering', review_count='2', agreed_to_form=True)
    site_user17 = SiteUser.objects.get_or_create(email='candra.bulger@emory.edu', password='123', first_name='Candra', last_name='Bulger', department='Biostatistics', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest='Computer science, Chemistry, Physics, Biostatistics', review_count='2', agreed_to_form=True)
    site_user18 = SiteUser.objects.get_or_create(email='sudie.benham@emory.edu', password='123', first_name='Sudie', last_name='Benham', department='Business', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest='Statistics, Machine learning', review_count='1', agreed_to_form=True)
    site_user19 = SiteUser.objects.get_or_create(email='jenna.geno@emory.edu', password='123', first_name='Jenna', last_name='Geno', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest='Mathematics, Machine learning', review_count='1', agreed_to_form=True)
    site_user20 = SiteUser.objects.get_or_create(email='heide.woodley@emory.edu', password='123', first_name='Heide', last_name='Woodley', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest='Mathematics, Statistics, Machine learning', review_count='1', agreed_to_form=True)

    ReviewPeriod.objects.all().delete()

    period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=1, day=10), review_deadline=datetime.date(year=2015, month=2, day=10), group_meeting_time=datetime.date(year=2015, month=2, day=25), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.')
    #period1 = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2015, month=3, day=1), review_deadline=datetime.date(year=2015, month=4, day=1), group_meeting_time=datetime.date(year=2015, month=5, day=1), group_meeting_venue='Room E404, MSC, Emory University, GA 30030.')
    Manuscript.objects.all().delete()


    manuscript4 = Manuscript.objects.get_or_create(keywords=['math','Physics'], title = 'LAD VS PDA5******', brief_title='LAD VS PDA4', abstract='ooooooo', review_period=period[0], field='Software Engineering', target_journal='target_journal', is_final=True)
    manuscript4[0].reviewers.add(site_user2[0])
    manuscript4[0].reviewers.add(site_user10[0])
    manuscript4[0].reviewers.add(site_user16[0])
    manuscript4[0].authors.add(site_user6[0])


    #manuscript1 = Manuscript.objects.get_or_create(id=1,keywords=['computer science','stat'], title = 'LAD VS PDA1*****', brief_title='LAD VS PDA1', abstract='ooooooo', review_period=period1[0], field='computer science', target_journal='target_journal')
    manuscript1 = Manuscript.objects.get_or_create(keywords=['face recognition', 'pattern recognition', 'principal components analysis', 'linear discriminant analysis', 'learning from undersampled distributions', 'small training data sets'], title = 'PCA versus LDA PCA versus LDA PCA versus LDA', brief_title='PCA versus LDA', abstract='In the context of the appearance-based paradigm for object recognition, it is generally believed that algorithms based on LDA (Linear Discriminant Analysis) are superior to those based on PCA (Principal Components Analysis). In this communication, we show that this is not always the case. We present our case first by using intuitively plausible arguments and, then, by showing actual results on a face database. Our overall conclusion is that when the training data set is small, PCA can outperform LDA and, also, that PCA is less sensitive to different training data sets.', review_period=period[0], field='computer science', target_journal='IEEE Transaction on Machine Learning', is_final=False)
    #print manuscript[0].keywords
    #print manuscript.review_period
    #manuscript[0].review_period.set(period1[0])
    manuscript1[0].reviewers.add(site_user1[0])
    manuscript1[0].reviewers.add(site_user19[0])
    manuscript1[0].authors.add(site_user3[0])



    manuscript2 = Manuscript.objects.get_or_create(keywords=['math','eco'], title = 'LAD VS PDA2******', brief_title='LAD VS PDA2', abstract='ooooooo', review_period=period[0], field='Mathematics', target_journal='target_journal')
    manuscript2[0].reviewers.add(site_user2[0])
    manuscript2[0].reviewers.add(site_user4[0])
    manuscript2[0].reviewers.add(site_user16[0])
    manuscript2[0].authors.add(site_user4[0])


    manuscript3 = Manuscript.objects.get_or_create(keywords=['math','Physics','finance'], title = 'LAD VS PDA3*****',brief_title='LAD VS PDA3', abstract='ooooooo', review_period=period[0], field='Physics', target_journal='target_journal')
    manuscript3[0].reviewers.add(site_user14[0])
    manuscript3[0].reviewers.add(site_user3[0])

    manuscript3[0].authors.add(site_user2[0])



    manuscript5 = Manuscript.objects.get_or_create(keywords=['math','eco','finance'], title = 'LAD VS PDA5*****',brief_title='LAD VS PDA5', abstract='ooooooo', review_period=period[0], field='Finance', target_journal='target_journal', is_final=True)
    manuscript5[0].reviewers.add(site_user5[0])
    manuscript5[0].reviewers.add(site_user6[0])
    manuscript5[0].reviewers.add(site_user7[0])
    manuscript5[0].reviewers.add(site_user8[0])
    manuscript5[0].reviewers.add(site_user9[0])
    manuscript5[0].authors.add(site_user10[0])

    #manuscript.title = 'LAD VS PDA'
    #manuscript.keywords.clean('cs','tt')


    #add_user(email='mary@emory.edu', first_name='Mary', last_name='Lee', department='Math & CS', lab='Gee\'s Lab', pi='Gee', review_count='3')
    return

def add_user(email, first_name, last_name, department, lab, pi, review_count):
    #email, password, first_name=None, last_name=None, department=None, lab=None, pi=None,
    #site_user = SiteUser.objects.create_user(email=email, first_name=first_name, last_name=last_name, department=department, lab=lab, pi=pi, Review_Count=review_count)[0]
    #site_user = SiteUser.objects.create_user(email=email, password=p)
    return

if __name__ == '__main__':
    print "Starting PeerReview population script..."
    populate()





















