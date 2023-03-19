"""
Views for the recipe API
"""

from rest_framework import viewsets # we are using viewset not apiview for the view
from rest_framework.authentication import TokenAuthentication # Authentication system been used
from rest_framework.permissions import IsAuthenticated # Permission we are checking before endpoint is used

from core.models import Recipe
from recipe import serializers



class RecipeViewSet(viewsets.ModelViewSet): # There are various viewsets available, the model view set is specifically set up to work directly with a model
  """View for manage recipe APIs"""
  serializer_class = serializers.RecipeSerializer

  # This represents the objects that are available for this viewset, since its a model view set, its expected to work with a model
  queryset = Recipe.objects.all()

  authentication_classes = [TokenAuthentication] # The system for authentication
  permission_classes = [IsAuthenticated] # The user has to be authenticated to use the api

  def get_queryset(self):
      """Retrieve recipes for authenticated user."""
      # We are overiding get_queryset, typically it would return all the objects in queryset above, but what we are doing is adding an additional filter, to filter by the user that is assigned to the request 
      return self.queryset.filter(user=self.request.user).order_by('-id')

