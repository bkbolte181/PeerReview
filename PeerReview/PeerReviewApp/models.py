from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from custom_fields import SeparatedValuesField
from datetime import datetime

class SiteUserManager(BaseUserManager):
	'''
		Manager for SiteUser model. This replaces the default manager used by Django, since the model
		is custom. The UserManager needs two methods, create_user and create_superuser. Most other methods
		are subclassed from BaseUserManager.
	'''
	def _create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		if not email:
			raise ValueError('An email must be provided to create the user.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
	def create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		return self._create_user(email, password)
		
	def create_superuser(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		return self._create_user(email, password)
Schools = (
	'GOIZUETA BUSINESS SCHOOL',
	'LANEY GRADUATE SCHOOL',
	'SCHOOL OF LAW',
	'SCHOOL OF MEDICINE',
	'NELL HODGSON WOODRUFF SCHOOL OF NURSING',
	'ROLLINS SCHOOL OF PUBLIC HEALTH',
	'CANDLER SCHOOL OF THEOLOGY',
)
Schools = [(x, x) for x in Schools]

class SiteUser(AbstractBaseUser):
	'''
		Custom User model. Set the user model to this one in the settings.py file:
		AUTH_USER_MODEL = 'PeerReviewApp.SiteUser' # Add this variable to settings.py file
		This will tell Django to use this model as the default user model. There are a fe
		required attributes for custom user models:
			-> USERNAME_FIELD: Unique identifier for log in (in this case, email)
			-> REQUIRED_FIELDS: Required fields (update this to include required fields)
			-> get_full_name(): Return the "full name" of the user
			-> get_short_name(): Return a "short name" identifier for the user
		Additionally, this model requires a custom user manager, and some custom handlers
		for forms to replace the built-ins that Django provides.
	'''
	email = models.EmailField('email address', max_length=200, unique=True,
		error_messages = {
			'unique': 'A user with that email already exists.',
		})
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	# Information about the user's scientific background
	department = models.CharField(max_length=200)
	lab = models.CharField(max_length=200)
	pi = models.CharField(max_length=200)
	school = models.CharField(max_length = 200, choices=Schools)

	NONE = '0'
	LESS_THAN_FIVE = '1'
	MORE_THAN_FIVE = '2'
	
	PAPERS_REVIEWED = (
		(NONE, 'None'),
		(LESS_THAN_FIVE, 'Less than 5'),
		(MORE_THAN_FIVE, 'More than 5'),
	)
	
	papers_reviewed = models.CharField(max_length=2, choices=PAPERS_REVIEWED, default=NONE)
	
	agreed_to_form = models.BooleanField(default=False) # Whether or not the user has agreed to to use form
	
	objects = SiteUserManager()
	
	# Required for custom user model
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	def get_full_name(self): return self.first_name, self.last_name
	def get_short_name(self): return self.first_name

class ReviewPeriod(models.Model):
	''' Model for a single review period '''
	is_full = models.BooleanField(default=False) # If this review period is full or not
	start_date = models.DateField(default=datetime.now()) # Date when this period becomes open
	submission_deadline = models.DateField() # Date when submissions are due
	review_deadline = models.DateField() # Date when reviews are due back
	group_meeting_time = models.DateField() # Large group meeting time

class Manuscript(models.Model):
	'''
		This is the model that links everything together. BEWARE! Errors kept popping up with the ManyToMany fields.
		There may be a better way to do this.
	'''
	reviewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="reviewers", related_query_name="reviewer")
	authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="authors", related_query_name="author")
	title = models.CharField(max_length=200, unique=True)
	keywords = SeparatedValuesField(max_length=1000, help_text='Keywords, separated by a comma') # Custom field for storing python lists
	review_period = models.ForeignKey(ReviewPeriod, related_name="manuscripts", related_query_name="manuscript")
	manuscript_file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), default='anonymous.jpg', help_text='Upload .zip file containing all relevant material')
	review_file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), default='anonymous.jpg', help_text='Upload .zip file containing all relevant material')