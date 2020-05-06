from rest_framework import serializers
from app.api.models import (
    Ep,
)
class EpSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Ep
        fields = ('id', 'name', 'description',
                  'owner', 'category',
                  'created_at', 'updated_at',
                  'is_public')
# class CategorySerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     recipes = RecipeSerializer(many=True, read_only=True, required=False)
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'owner',
#                   'description', 'recipes',
#                   'created_at', 'updated_at')