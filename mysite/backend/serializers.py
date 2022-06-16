from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
"""
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
"""
class DomainCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainCredentials
        fields = '__all__'  
"""
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  
"""
class PurchasedDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedDomain
        fields = '__all__'  
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  