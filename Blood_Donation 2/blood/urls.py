from . import views
# from blood.models import
from django.conf.urls import url


urlpatterns = [
	url(r'^home/$', views.index, name='index'),
	url(r'^aboutus/$', views.aboutus, name='aboutus'),

	
	url(r'^home/(?P<pk>\d+)/$', views.details, name='details'),


	# CRUD on Blood Clients
	url(r'^home/Blood-Donor/Add/$', views.add_donor, name='add_donor'),
	url(r'^home/(?P<pk>\d+)/edit/$', views.edit_donor, name='edit_donor'),

	# Sorted
	url(r'^home/Blood-Donor/Blood-Group-A/$', views.blood_client_A, name="blood_group_a"),


	# LOGGING
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

] 









