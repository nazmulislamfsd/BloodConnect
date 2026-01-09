from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import CustomUserManager
from cloudinary.models import CloudinaryField
# from blood.models import BloodGroup

# Create your models here.

# User Model (Donor)
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField()
    blood_group = models.ForeignKey('blood.BloodGroup', on_delete=models.CASCADE, related_name='users')
    are_you_donor = models.BooleanField()
    last_donate = models.DateField(blank=True, null=True)
    availability_status = models.BooleanField(default=False)
    # profile
    profile_image = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' # Use email instead of username
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email