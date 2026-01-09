from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blood.views import BloodGroupViewSet, BloodRequestViewSet, DonationHistoryViewSet
from user.views import DonorViewSet

router = DefaultRouter()
router.register('blood-groups', BloodGroupViewSet, basename='blood-group')
router.register('blood-requests', BloodRequestViewSet, basename='blood-request')
router.register('donation-history', DonationHistoryViewSet, basename='donation-history')
router.register('donors', DonorViewSet, basename='donor')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]