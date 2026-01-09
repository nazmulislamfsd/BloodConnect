from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# blood category/group
class BloodGroup(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

# blood request post(Event)
class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    hospital_name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_requests')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    number_of_units = models.IntegerField()
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='blood_requests')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Has the donor been found or not?
    donor_found = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.patient_name} ({self.blood_group})'
    

# Donation History
class DonationHistory(models.Model):
    DONATION_HISTORY_STATUS = [
        ('RECEIVED', 'Received'),
        ('CANCELED', 'Canceled'),
        ('DONATED', 'Donated'),
    ]
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation_histories')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=DONATION_HISTORY_STATUS, default='RECEIVED')

    def __str__(self):
        return f'Donor: {self.donor} - Receiver: {self.receiver} - Status: {self.status}'