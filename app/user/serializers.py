"""
Serializers for the user API View
"""

from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext as _ # Import translations

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

class AuthTokenSerializer(serializers.Serializer):
  """Serializer for the user auth token"""
  email = serializers.EmailField() # Required field email
  password = serializers.CharField( # Required field password
    style={'input_type': 'password'}, # Hides password in browsable API while typing
     # This ensures we dont trim whitespace at the end of the password
    trim_whitespace = False
  )

  def validate(self, attrs):
    """Validate and authenticate the user."""
    email = attrs.get('email') # Retrieve email and password that user provides
    password = attrs.get('password')
    user = authenticate(
      request=self.context.get('request'),
      username=email, # we set username to the email address, per django uses username by defailt
      password=password
    )

    if not user:
      msg = _('Unable to authenticate with provided credentials.')
      raise serializers.ValidationError(msg, code='authorization') # Standard way to raise error in serializers, the view would translate it to a HTPP 400 request

    attrs['user'] = user
    return attrs