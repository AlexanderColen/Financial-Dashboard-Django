"""
Serializers for encoding/decoding User & Group models.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for Group model.
    """
    class Meta:
        model = Group
        fields = ['name']
