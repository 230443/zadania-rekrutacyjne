from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'color', 'is_male']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cats = CatSerializer(source='cat_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'cats']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
