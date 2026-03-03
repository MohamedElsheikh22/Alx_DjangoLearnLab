from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')
        extra_kwargs = {'email': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password didn't match."})
        return attrs
    
    def create(self, validate_data):
        validate_data.pop('password2')
        password = validate_data.pop('password')
        user = User(**validate_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')
        read_only_fields = ('id', 'username', 'followers')
