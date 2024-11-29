from rest_framework import serializers
from base.models import Item

class ItemSerializers_allFields(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'code']
