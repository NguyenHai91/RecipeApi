
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe import serializers

# Create your views here.
class TagViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Tag.objects.all()
  serialzier_class = serializers.TagSerializer

  def get_queryset(self):
    return self.queryset.filter(user=self.request.user).order_by('-name')

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class IngredientViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):

  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Ingredient.objects.all()
  serializer_class = serializers.IngredientSerializer

  def get_queryset(self):
    return self.queryset.filter(user=self.request.user).order_by('-name')