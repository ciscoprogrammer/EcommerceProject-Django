from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Address
from .serializers import UserSerializer, AddressSerializer
from rest_framework import generics
from .models import Profile, Address
from .serializers import ProfileSerializer, AddressSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal, InvalidOperation
from .models import Profile

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal
from .models import Profile

@api_view(['POST'])
def update_revenue(request, user_id):
    try:
        profile = Profile.objects.get(user__id=user_id)
    except Profile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    amount = request.data.get('amount', None)
    if not amount:
        return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount_decimal = Decimal(amount)
    except InvalidOperation:  
        return Response({'error': 'Invalid amount format'}, status=status.HTTP_400_BAD_REQUEST)

    profile.revenue += amount_decimal
    profile.save()

    return Response({'message': 'Revenue updated successfully', 'new_revenue': profile.revenue}, status=status.HTTP_200_OK)
