from rest_framework.permissions import BasePermission, SAFE_METHODS

# donation history permission
class ReadOnlyOrReceiverOrAdmin(BasePermission):
    message = "Only receiver or admin can modify this donation history."

    def has_object_permission(self, request, view, obj):
        # Read-only access (GET, HEAD, OPTIONS) → সবাই পারবে
        if request.method in SAFE_METHODS:
            return True

        # Admin access
        if request.user.is_staff or request.user.is_superuser:
            return True

        # Receiver access
        return obj.receiver == request.user
    

# blood-request permission
class ReadOnlyOrRequesterOrAdmin(BasePermission):
    message = "Only requester or admin can modify this blood request."

    def has_object_permission(self, request, view, obj):

        # Read-only access (GET, HEAD, OPTIONS) → সবাই পারবে
        if request.method in SAFE_METHODS:
            return True
        # Admin access
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Requester access
        return obj.requester == request.user
    
    def has_permission(self, request, view):
        # Read-only access (GET, HEAD, OPTIONS) → সবাই পারবে
        if request.method in SAFE_METHODS:
            return True
        # Authenticated user hle POST method chalaite parbe
        if request.user.is_authenticated:
            return True
        # Admin access
        if request.user.is_staff or request.user.is_superuser:
            return True



# blood group permission
class BloodGroupPermission(BasePermission):

    message = "Only admin can modify this blood group."

    def has_object_permission(self, request, view, obj):
        # Read-only access (GET, HEAD, OPTIONS) → সবাই পারবে
        if request.method in SAFE_METHODS:
            return True
        # Admin access
        if request.user.is_staff or request.user.is_superuser:
            return True
        
    def has_permission(self, request, view):
        # Read-only access (GET, HEAD, OPTIONS) → সবাই পারবে
        if request.method in SAFE_METHODS:
            return True
        # Admin access
        if request.user.is_staff or request.user.is_superuser:
            return True