from rest_framework import serializers
from core.models.subscriber import SubscriberModel


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return SubscriberModel.objects.create(**validated_data)
