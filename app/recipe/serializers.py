"""
Serializers for recipe APIs
"""

from rest_framework import serializers
from core.models import Recipe

# The serializer represents a particular model (the recipe model)
# Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. 
class RecipeSerializer(serializers.ModelSerializer):
  """Serializer for recipes"""

  class Meta:
    model = Recipe # Tells django we are using the Recipe model with the serializer
    fields = ['id', 'title', 'time_minutes', 'price', 'link'] # The fields been used
    read_only_fields = ['id'] # The field that wouldnt be changed