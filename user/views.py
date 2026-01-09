from user.serializers import DonorSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# Create your views here.

# donor view set
class DonorViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = DonorSerializer
    queryset = User.objects.filter(are_you_donor=True)
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blood_group', 'age', 'availability_status']