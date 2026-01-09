from rest_framework.serializers import ModelSerializer
from blood.models import BloodGroup, BloodRequest, DonationHistory

# blood group serializer
class BloodGroupSerializer(ModelSerializer):
    class Meta:
        model = BloodGroup
        fields = ['id', 'name', 'description']



# blood request serializer(POST)
class BloodRequestSerializer(ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = ['id', 'patient_name', 'patient_age', 'hospital_name', 'location', 'email', 'phone', 'number_of_units', 'blood_group', 'description']


# blood request serializer(GET)
class BloodRequestViewSerializer(ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = ['id', 'patient_name', 'patient_age', 'requester', 'hospital_name', 'location', 'email', 'phone', 'number_of_units', 'blood_group', 'description']

    
class DonationHistorySerializer(ModelSerializer):
    class Meta:
        model = DonationHistory
        fields = ['id', 'donor', 'receiver', 'status']

# donation history update
class DonationHistoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = DonationHistory
        fields = ['status']
