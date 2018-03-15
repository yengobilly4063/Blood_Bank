from django.contrib import admin
from blood.models import Country, Region, Hospital, Blood_Group, Blood_Client, Approved

# Register your models here.

class Blood_ClientAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'age', 'country', 'hospital', 'blood_group', 'approved')
	list_filter = ('country', 'hospital', 'blood_group')
	# search_fields = ('blood_group', 'hospital', '<country></country>')

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Hospital)
admin.site.register(Blood_Group)
admin.site.register(Blood_Client, Blood_ClientAdmin)
admin.site.register(Approved)



