from blood.models import Blood_Client, Blood_Group, Country, Region, Hospital
# from django.forms import ModelForm


# class Blood_ClientForm(ModelForm):
# 	class Meta:
# 		model = Blood_Client
# 		fields = ['first_name', 'last_name', 'age', 'country', 'region', 'hospital',]

# # Create a form instance from POST data
# form = Blood_ClientForm(request.POST)


# # Save shis form instance from  the POST data to the database from the Blood_ClientForm object form
# new_client = form.save()


# # Create a form to edit the existing Blood_Client and
# # Get data from the request.Post to populate the bound form

# a = Blood_Client.objects.get(pk=request.pk)
# form = Blood_ClientForm(request.POST, instance=a)
# form.save()

from django import forms

class BloodClientForm(forms.ModelForm):
	class Meta:
		model = Blood_Client
		fields = ['first_name', 'last_name', 'age', 'image', 'blood_group', 'country', 'region', 'hospital']







































