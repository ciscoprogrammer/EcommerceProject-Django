from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address
from .models import Profile, Address



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # This means all fields of the model will be included.


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=False)  # OneToOne relationship
    addresses = AddressSerializer(read_only=True, many=True)  # ForeignKey relationship
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','profile','addresses']
