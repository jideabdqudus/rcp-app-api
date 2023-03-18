"""
Serializers for the user API View
"""

from django.contrib.auth import get_user_model

# Import the serializer module from the rest_framework (serializers are basically a way to convert a json object to and from python, there are different base classes, we are using the serializers.ModelSerializer)
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
  """Serializer for the user object."""

  class Meta:
    model = get_user_model() # get the model it would be representing
    fields = ['email', 'password', 'name'] # what are the actual fields that will be provided in the request that should be saved in the model
    extra_kwargs = {'password': {'write_only': True, 'min_length': 5}} # A dictionary to provide extra metadata to the fields

  def create(self, validated_data):
    """Create and return a user with encrypted password"""
    return get_user_model().objects.create_user(**validated_data)