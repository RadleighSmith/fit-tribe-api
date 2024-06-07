from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.

    This serializer handles the serialization and deserialization of Follower objects,
    including validation to ensure that duplicate follower relationships are not created.

    Attributes:
        follower (ReadOnlyField): The username of the user who is following another user.
        followed_name (ReadOnlyField): The username of the user who is being followed.

    Methods:
        create(validated_data): Custom create method to handle IntegrityError and provide a user-friendly error message.
    """
    follower = serializers.ReadOnlyField(source='follower.username')
    followed_name = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following', 'created_at', 'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'This follow relationship already exists.'})

