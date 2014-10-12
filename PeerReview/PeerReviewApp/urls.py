from django.conf.urls import patterns, include, url
from PeerReviewApp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^terms/$', views.terms, name='terms'), # Eventually change this to point at 'terms of service' view
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.auth_login, name='login'),
	url(r'^account/$', views.account, name='account'),
	url(r'^logout/$', views.auth_logout, name='logout'),
	url(r'^upload/$', views.uploader_home, name='upload'),
	url(r'^review/$', views.reviewer_home, name='review'),
	url(r'^agreement/$', views.agreement, name='agreement'),
)