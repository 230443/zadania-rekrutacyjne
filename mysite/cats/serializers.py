from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Cat, Hunting, Prey


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


class PreySerializer(serializers.ModelSerializer):
    class Meta:
        model = Prey
        fields = ['type']


class HuntingSerializer(serializers.ModelSerializer):
    preys = PreySerializer(source='prey_set', many=True)

    class Meta:
        model = Hunting
        fields = ['cat', 'start_date', 'duration', 'preys']

    def create(self, validated_data):
        print(self.data)
        preys_data = validated_data.pop('prey_set')
        hunting = Hunting.objects.create(**validated_data)

        for prey_data in preys_data:
            Prey.objects.create(hunting=hunting, **prey_data)

        hunting.save()
        return hunting
