from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.

class Country(models.Model):
	COUNTRY = (
			('CM', 'Cameroon'),
			('EG', 'Equetorial Guinnea'),
			('USA', 'United States'),
		)
	country = models.CharField(choices=COUNTRY, help_text="PLease enter country of origin", max_length=3)

	def __str__(self):
		return self.country

class Region(models.Model):
	REGIONAL_LOCATION = (
			# More choices will be added with time i.e. Still to be poppulated
			('NW', 'North-West'),
			('SW', 'South-West'),
			('LT', 'Littoral'),
		)
	region = models.CharField(choices=REGIONAL_LOCATION, help_text="Region of origin", max_length=3)

	def __str__(self):
		return self.region

class Hospital(models.Model):
	HOSPITAL_CHOICES = (
			# More choices will be added with time i.e. Still to be poppulated
			('MBH', 'Mbingo Baptist Hospital (MBH)'),
			('BBH', 'Banso Baptist Hospital (BBH)'),
		)
	hospital = models.CharField(choices=HOSPITAL_CHOICES, help_text="Hospital of/for blood examination", max_length=3)
	
	def __str__(self):
		return self.hospital

class Blood_Group(models.Model):
	blood_type = (
			('A+','A+'),
			('B+','B+'),
			('AB','AB - Universal Recipient'),
			('O+','O+ - Universal Donor'),
			('A-','A-'),
			('B-','B-'),
			('O-','O-'),
		)
	blood_group = models.CharField(choices=blood_type, max_length=2, default='O', help_text="What blood group are you?")

	def __str__(self):
		return self.blood_group

class Approved(models.Model):
	approved_choices = (
		('True','True'),
		('False','False')
	)
	approved = models.CharField(choices=approved_choices, max_length=5, default='False')

	def __str__(self):
		return self.approved



class Blood_Client(models.Model):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	age = models.IntegerField()

	# Functions
	def fullName(self):
	 return "{} {}".format(self.first_name, self.last_name)


	image = models.FileField()


	# def age(self):
	# 	return datetime.today.now() - self.date_of_birrh

	# Relationships
	blood_group = models.ForeignKey(Blood_Group, on_delete=models.SET_NULL, null=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
	hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)

	# Creation/Modification dates
	created = models.DateTimeField(auto_now_add=True) 
	modified = models.DateTimeField(auto_now=True)
	
	# Determines if Blood Client info is approved or not
	approved = models.ForeignKey(Approved, on_delete=models.SET_NULL, null=True)

	def get_absolute_url(self):
		return reverse('blood:details', kwargs={'pk': self.id})

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)



































