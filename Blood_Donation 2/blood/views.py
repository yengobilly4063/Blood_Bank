from django.shortcuts import render, redirect, get_object_or_404
from blood.models import Blood_Client, Blood_Group, Country, Region, Hospital, Approved
from django.http import HttpResponse, HttpResponseRedirect

# For user authentication and authorization
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from blood.forms import BloodClientForm

# Create your views here.



def index(request):
	client_list = Blood_Client.objects.all().order_by('-created')																																																																																																																																																																
	context = {'client_list':client_list,}
	return render(request, 'blood/home.html', context)


def details(request, pk):
	client = Blood_Client.objects.get(pk=pk)
	context = {'client':client}
	return render(request, 'blood/blood_client_details.html', context )



def aboutus(request):
	return render(request, 'blood/aboutus.html')



def add_donor(request):
	if request.method == 'POST':
		form = BloodClientForm(request.POST or None, request.FILES)
		if form.is_valid():
			donor = form.save(commit=False)
			donor.save()
			return HttpResponseRedirect(donor.get_absolute_url())
	else:
		form = BloodClientForm()
	context = {'form':form}
	return render(request, 'blood/add_donor.html', context)



def edit_donor(request, pk=None):
	client = get_object_or_404(Blood_Client, pk=pk)
	if request.method == 'POST':
		form = BloodClientForm(request.POST, request.FILES, instance=client)
		if form.is_valid():
			donor = form.save(commit=False)
			donor.save()
			# return redirect('blood:details', pk)
			# Message Success
			return HttpResponseRedirect(donor.get_absolute_url())
	else:
		form = BloodClientForm(instance=client)
	context = {'form':form, 'client':client}
	template = 'blood/edit_donor.html'
	return render(request, template, context)



# Blood Donor Pages based on Filters of blood group or Country of origin
def blood_client_A(self):
	clients = Blood_Client.objects.filter(blood_group="A")
	context = {'clients':clients}
	template = 'blood/blood_client_A+.html'
	return render(request, template, context)



# LOGGING : login and logout
def login(request):
	return render(request, 'registration/login.html')

def logout(request):
	return render(request, 'registration/logout.html')










