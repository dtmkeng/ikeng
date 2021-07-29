from rest_framework import serializers
from ikeng.core.models.subscriber import SubscriberModel
from ikeng.core.models.profile import Profile
from ikeng.core.models.post import (
    Post,
    Comment,
)


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return SubscriberModel.objects.create(**validated_data)


class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class Commentserailizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerailizer(serializers.ModelSerializer):
    commen = Commentserailizer(source='comment', many=True)
    class Meta:
        model = Post
        fields = '__all__'
