from rest_framework import serializers
from .models import User,Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'full_name', 'address_1', 'city', 'zipcode', 'country', 'phone', 'date_joined')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    #profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'email','password', 'is_staff', 'is_active', 'profile')
        extra_kwargs = {'password': {'write_only': True,'required': True}}
'''
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user
        
        
        existing_profile = Profile.objects.filter(user=user).first()

        if existing_profile:
            # Update existing profile
            for attr, value in profile_data.items():
                setattr(existing_profile, attr, value)
            existing_profile.save()
        else:
            # Create new profile
            Profile.objects.create(user=user, **profile_data)

        return user
        '''
        