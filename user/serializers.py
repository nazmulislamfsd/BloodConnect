from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# custom user serializer (***READ OPERATION)
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password', 'address', 'phone', 'age', 'blood_group', 'last_donate', 'availability_status', 'are_you_donor', 'profile_image', 'bio', 'created_at', 'updated_at']




# custom user create serializer(***WRITE OPERATION)
class CustomUserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'blood_group', 'email', 'password', 'are_you_donor']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        
        user.set_password(password)
        user.save()
        
        return user
    

# custom user update serializer (***UPDATE OPERATION)
class CustomUserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'phone', 'age', 'blood_group', 'last_donate', 'availability_status', 'are_you_donor', 'profile_image', 'bio']

# donor serializer
class DonorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phone', 'age', 'blood_group', 'last_donate', 'availability_status', 'are_you_donor', 'profile_image', 'bio']

