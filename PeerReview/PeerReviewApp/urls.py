from django.conf.urls import patterns, include, url
from django.conf import settings
from PeerReviewApp import views

adminpatterns = patterns('',
	url(r'^$', views.auth_admin, name='admin_home')
)

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^admin/$', include(adminpatterns)),
	url(r'^terms/$', views.terms, name='terms'), # Eventually change this to point at 'terms of service' view
	url(r'^edit/(?P<mid>\d+)/$', views.edit_manuscript, name='edit_manuscript'),
	url(r'^about/$', views.about, name='about'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.auth_login, name='login'),
	url(r'^account/$', views.account, name='account'),
	url(r'^logout/$', views.auth_logout, name='logout'),
	url(r'^remove/(?P<fid>\d+)/$', views.remove_associated_file, name='remove_associated_file'),
	url(r'^author/$', views.author_home, name='authorhome'),
	url(r'^review/$', views.reviewer_home, name='review'),
	url(r'^browse/(?P<current_page>\d+)/$',views.browse_manuscripts, name='browse'),
	url(r'^agreement/$', views.agreement, name='agreement'),
    url(r'^assignedmanuscripts/(?P<current_page>\d+)/$',views.assigned_manuscripts, name='assigned_manuscripts'),
	url(r'^uploadmanuscript/$', views.upload_manuscript, name='upload_manuscript'),
	# Media root for serving files when on a local dev server
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
