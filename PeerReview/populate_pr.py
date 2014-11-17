import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeerReview.settings')

import django
django.setup()

from PeerReviewApp.models import SiteUser, ReviewPeriod, Manuscript
import datetime

def populate():
    #SiteUser.objects.all().delete()
    #user1 = SiteUser.objects.get(email='mary1@emory.edu')
    #print user1
    #user1.delete()
    #SiteUser.objects.all().delete()

    #SiteUser.objects.get(email='mary1@emory.edu').delete()
    site_user1 = SiteUser.objects.get_or_create(email='mary1@emory.edu', password='123', first_name='Mary1', last_name='Lee1', department='Math & CS1', lab='Gee\'s Lab1', pi='Gee\'s PI1', research_interest=['computer science','Software Engineering'], review_count='5', agreed_to_form=True)
    #SiteUser.objects.get(email='mary2@emory.edu').delete()
    site_user2 = SiteUser.objects.get_or_create(email='mary2@emory.edu', password='123', first_name='Mary2', last_name='Lee2', department='Math & CS2', lab='Gee\'s Lab2', pi='Gee\'s PI2', research_interest=['computer science','Bios'], review_count='3', agreed_to_form=True)
    #SiteUser.objects.get(email='mary3@emory.edu').delete()
    site_user3 = SiteUser.objects.get_or_create(email='mary3@emory.edu', password='123', first_name='Mary3', last_name='Lee3', department='Math & CS3', lab='Gee\'s Lab3', pi='Gee\'s PI3', research_interest=['STAT','FINANCE'], review_count='4', agreed_to_form=True)
    #SiteUser.objects.get(email='mary4@emory.edu').delete()
    site_user4 = SiteUser.objects.get_or_create(email='mary4@emory.edu', password='123', first_name='Mary4', last_name='Lee4', department='Math & CS4', lab='Gee\'s Lab4', pi='Gee\'s PI4', research_interest=['ECO','MATH'], review_count='2', agreed_to_form=True)
    #SiteUser.objects.get(email='mary5@emory.edu').delete()
    site_user5 = SiteUser.objects.get_or_create(email='mary5@emory.edu', password='123', first_name='Mary5', last_name='Lee5', department='Math & CS5', lab='Gee\'s Lab5', pi='Gee\'s PI5', research_interest=['ECO','MATH'], review_count='1', agreed_to_form=True)

    ReviewPeriod.objects.all().delete()

    period = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2001, month=1, day=1), review_deadline=datetime.date(year=2001, month=1, day=1), group_meeting_time=datetime.date(year=2001, month=1, day=1), group_meeting_venue='Math & CS Building')
    period1 = ReviewPeriod.objects.get_or_create(submission_deadline=datetime.date(year=2002, month=1, day=1), review_deadline=datetime.date(year=2004, month=1, day=1), group_meeting_time=datetime.date(year=2003, month=1, day=1), group_meeting_venue='Math & CS Building 1')
    Manuscript.objects.all().delete()
    manuscript1 = Manuscript.objects.get_or_create(id=1,keywords=['computer science','stat'], title = 'LAD VS PDA1*****', brief_title='LAD VS PDA1', abstract='ooooooo', review_period=period1[0], field='computer science', target_journal='target_journal')
    #print manuscript[0].keywords
    #print manuscript.review_period
    #manuscript[0].review_period.set(period1[0])
    manuscript1[0].reviewers.add(site_user1[0])
    manuscript1[0].reviewers.add(site_user2[0])
    manuscript1[0].authors.add(site_user3[0])



    manuscript2 = Manuscript.objects.get_or_create(id=2,keywords=['math','eco'], title = 'LAD VS PDA2******', brief_title='LAD VS PDA2', abstract='ooooooo', review_period=period1[0], field='computer science', target_journal='target_journal')
    manuscript2[0].reviewers.add(site_user2[0])
    manuscript2[0].reviewers.add(site_user3[0])
    manuscript2[0].reviewers.add(site_user5[0])
    manuscript2[0].authors.add(site_user4[0])


    manuscript3 = Manuscript.objects.get_or_create(id=3,keywords=['math','eco','finance'], title = 'LAD VS PDA3*****',brief_title='LAD VS PDA3', abstract='ooooooo', review_period=period1[0], field='computer science', target_journal='target_journal')
    manuscript3[0].reviewers.add(site_user4[0])
    manuscript3[0].reviewers.add(site_user5[0])

    manuscript3[0].authors.add(site_user2[0])

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





















