from rest_framework import serializers
from ikeng.core.models.subscriber import SubscriberModel
from ikeng.core.models.profile import Profile


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return SubscriberModel.objects.create(**validated_data)


class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
