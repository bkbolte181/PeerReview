from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Manuscript)
admin.site.register(SiteUser)
admin.site.register(ReviewPeriod)

