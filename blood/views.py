from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from blood.models import BloodGroup, BloodRequest, DonationHistory
from blood.serializers import BloodGroupSerializer, BloodRequestSerializer, BloodRequestViewSerializer, DonationHistorySerializer, DonationHistoryUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from blood.permissions import ReadOnlyOrReceiverOrAdmin, ReadOnlyOrRequesterOrAdmin, BloodGroupPermission
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

'''Create your views here.'''

# blood group view
class BloodGroupViewSet(ModelViewSet):
    '''
    Blood Group Management API.

    এই API ব্যবহার করে রক্তের গ্রুপ সংক্রান্ত তথ্য:
    - সব Blood Group দেখা যাবে
    - নতুন Blood Group যোগ করা যাবে - (Admin)
    - নির্দিষ্ট Blood Group আপডেট করা যাবে - (Admin)
    - Blood Group ডিলিট করা যাবে - (Admin)

    '''

    http_method_names = ['get', 'post', 'put', 'delete']

    serializer_class = BloodGroupSerializer
    queryset = BloodGroup.objects.all()
    permission_classes = [BloodGroupPermission]




# blood request view
class BloodRequestViewSet(ModelViewSet):
    """
    Blood Request Management API.

    এই API এর মাধ্যমে:
    - রক্তের অনুরোধ (Blood Request) তৈরি করা যাবে - (Authenticated User)
    - সব রক্তের অনুরোধ দেখা যাবে
    - নির্দিষ্ট রক্তের অনুরোধ আপডেট করা যাবে - (Only Requester or Admin)
    - রক্তের অনুরোধ ডিলিট করা যাবে - (Only Requester or Admin)
    - রক্তের অনুরোধ একসেপ্ট করতে পারবে - (Authenticated User)
    """

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            return BloodRequestViewSerializer
        return BloodRequestSerializer
    
    queryset = BloodRequest.objects.all()
    permission_classes = [ReadOnlyOrRequesterOrAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        blood_request = serializer.save(requester=request.user)

        return Response(
            BloodRequestViewSerializer(blood_request).data
        )


    @action(detail=True, methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def accept(self, request, pk=None):
        donor = request.user    # donor
        blood_request = BloodRequest.objects.get(id=pk)
       
        requester = blood_request.requester
        receiver = requester

        donation_history = DonationHistory.objects.create(donor=donor, receiver=receiver)

        blood_request.donor_found = True
        blood_request.save()

        return Response(
            DonationHistorySerializer(donation_history).data
        )


# donation history view
class DonationHistoryViewSet(ModelViewSet):
    """
    Donation History Management API.

    এই API এর মাধ্যমে:
    - রক্ত দানের ইতিহাস (Donation History) সংরক্ষণ করা যাবে
    - সব রক্ত দানের ইতিহাস দেখা যাবে
    - নির্দিষ্ট দানের তথ্য আপডেট করা যাবে - (Only Receiver or Admin)
    - দানের তথ্য ডিলিট করা যাবে - (Only Receiver or Admin)
    - নির্দিষ্ট ব্যক্তির রক্তদানের ইতিহাস দেখা যাবে
    """

    http_method_names = ['get', 'put', 'patch', 'delete']

    def get_queryset(self):
        return DonationHistory.objects.all()
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return DonationHistoryUpdateSerializer
        return DonationHistorySerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    permission_classes = [ReadOnlyOrReceiverOrAdmin]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_donation_history(self, request, pk=None):
        donor = self.request.user.id
        
        donation_history = DonationHistory.objects.filter(donor=donor)

        return Response(
            DonationHistorySerializer(donation_history, many=True).data
        )