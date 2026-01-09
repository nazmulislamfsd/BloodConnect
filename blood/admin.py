from django.contrib import admin
from blood.models import BloodGroup, BloodRequest, DonationHistory

# Register your models here.
admin.site.register(BloodGroup)
admin.site.register(BloodRequest)
admin.site.register(DonationHistory)