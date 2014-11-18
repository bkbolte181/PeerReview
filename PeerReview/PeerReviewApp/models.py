from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from custom_fields import SeparatedValuesField
from datetime import datetime

SCHOOLS = (
	'Goizueta Business School',
	'Laney Graduate School',
	'School of Law',
	'Schoolf of Medicine',
	'Nell Hodgson Woodruff School of Nursing',
	'Rollins School of Public Health',
	'Candler School of Theology',
	'College of Arts and Sciences',
	'Other',
)

NONE = '0'
LESS_THAN_FIVE = '1'
MORE_THAN_FIVE = '2'

PAPERS_REVIEWED = (
	(NONE, 'None'),
	(LESS_THAN_FIVE, 'Less than 5'),
	(MORE_THAN_FIVE, 'More than 5'),
)

class SiteUserManager(BaseUserManager):
	'''
		Manager for SiteUser model. This replaces the default manager used by Django, since the model
		is custom. The UserManager needs two methods, create_user and create_superuser. Most other methods
		are subclassed from BaseUserManager.
	'''
	def _create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, research_interest=None, **extra_fields):
		if not email:
			raise ValueError('An email must be provided to create the user.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
	def create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, research_interest=None, **extra_fields):
		return self._create_user(email, password)
		
	def create_superuser(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, research_interest=None, **extra_fields):
		return self._create_user(email, password)

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
		error_messages={
			'unique': 'A user with that email already exists.',
		}, help_text="Emory Email Address")
	first_name = models.CharField(max_length=100, help_text="First Name")
	last_name = models.CharField(max_length=100, help_text="Last Name")

	@property
	def is_superuser(self):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin
	@property
	def is_admin(self):
		return True	
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin		
		
		
		
	# Information about the user's scientific background
	department = models.CharField(max_length=200, help_text="Department")
	lab = models.CharField(max_length=200, help_text="Name of Lab")
	pi = models.CharField(max_length=200, help_text="Name of Primary Investigator")
	school = models.CharField(max_length=100, choices=[(x, x) for x in SCHOOLS], default=SCHOOLS[0])
	review_count = models.CharField(max_length=2, help_text = "Number of Manuscripts you have reviewed", default=0)
	agreed_to_form = models.BooleanField(default=False) # Whether or not the user has agreed to to use form
	#added by admin
	#research_interest = SeparatedValuesField(max_length=1000, help_text='Research interests, separated by a comma',default=NONE) # Custom field for storing python lists
	research_interest = models.CharField(max_length=200, help_text="Research interests, separated by a comma")


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
	# added by admin
	group_meeting_venue = models.CharField(max_length=200)

class Manuscript(models.Model):
	'''
		This is the model that links everything together. BEWARE! Errors kept popping up with the ManyToMany fields.
		There may be a better way to do this.
	'''
	reviewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="reviewers", related_query_name="reviewer")
	authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="authors", related_query_name="author")
	status = models.CharField(max_length=20, default='submitted')

	# Semantic elements
	title = models.CharField(max_length=200, unique=True)
	brief_title = models.CharField(max_length=50, unique=True,default='')
	abstract = models.CharField(max_length=200000)
	keywords = SeparatedValuesField(max_length=1000, help_text='Keywords, separated by a comma') # Custom field for storing python lists
	field = models.CharField(max_length=200,default='')
	target_journal = models.CharField(max_length=200,default='')

	# Link to review period
	review_period = models.ForeignKey(ReviewPeriod, related_name="manuscripts", related_query_name="manuscript", default=0)
	is_final = models.BooleanField(default=False) # If the final decision of this manuscript has been made
























