from rest_framework import serializers
from .models import Hero

#Here we are converting JSON to a database model and reciprocally
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')