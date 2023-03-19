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

# We are using RecipeSerializer as the Param becuase the RecipeDetailSerializer is simply an extension of the RecipeSerializer above, so what we want to do is take the functionality of the recipe serializer and simply just add some extra fields for the RecipeDetail Serializer
class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    # We get all the meta value that were provided in the RecipeSeializer
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']