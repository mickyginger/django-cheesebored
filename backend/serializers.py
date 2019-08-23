from rest_framework import serializers
from django.contrib.auth.models import User
from jwt_auth import serializers as jwt_serializers
from .models import Cheese

class BaseCheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = ('id', 'name', 'origin', 'image', 'tasting_notes')



class CheeseSerializer(serializers.ModelSerializer):

    user = jwt_serializers.UserSerializer(read_only=True)

    class Meta:
        model = Cheese
        fields = (*BaseCheeseSerializer.Meta.fields, 'user')



class UserSerializer(jwt_serializers.UserSerializer):

    cheeses = BaseCheeseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'cheeses')
