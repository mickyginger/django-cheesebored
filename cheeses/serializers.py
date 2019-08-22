from rest_framework import serializers
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Cheese

class BaseCheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = ('id', 'name', 'origin', 'image', 'tasting_notes')



class BaseUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        data['password'] = make_password(password)
        return data


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation')



class CheeseSerializer(serializers.ModelSerializer):

    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Cheese
        fields = (*BaseCheeseSerializer.Meta.fields, 'user')



class UserSerializer(serializers.ModelSerializer):

    cheeses = BaseCheeseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (*BaseUserSerializer.Meta.fields, 'cheeses')
