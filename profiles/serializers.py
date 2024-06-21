from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer handles the serialization and deserialization of Profile objects,
    including additional computed fields for ownership, blog count, workout count,
    following status, follower counts, and group count.

    Attributes:
        owner (ReadOnlyField): The username of the profile owner.
        email (ReadOnlyField): The email of the profile owner.
        is_owner (SerializerMethodField): Indicates if the requesting user is the owner of the profile.
        blogs_count (ReadOnlyField): The number of blogs created by the profile owner.
        workouts_count (ReadOnlyField): The number of workouts created by the profile owner.
        following_id (SerializerMethodField): The ID of the following relationship if the requesting user follows the profile owner.
        following_count (ReadOnlyField): The number of users the profile owner is following.
        followers_count (ReadOnlyField): The number of users following the profile owner.
        display_name (BooleanField): Indicates if the real name should be displayed on the profile.

    Methods:
        get_is_owner(obj): Checks if the requesting user is the owner of the profile.
        get_following_id(obj): Gets the ID of the following relationship if the requesting user follows the profile owner.
        update(instance, validated_data): Handles the update process including updating the user's email.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.EmailField(source='owner.email', required=False)
    is_owner = serializers.SerializerMethodField()
    blogs_count = serializers.ReadOnlyField()
    workouts_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    display_name = serializers.BooleanField(required=False)

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of this profile.

        Args:
            obj (Profile): The profile object being serialized.

        Returns:
            bool: True if the current user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        """
        Get the ID of the 'Follower' instance if the current user follows the profile owner.

        Args:
            obj (Profile): The profile object being serialized.

        Returns:
            int or None: The ID of the 'Follower' instance if the current user follows the profile owner,
                         None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def update(self, instance, validated_data):
        """
        Update the Profile instance and the associated user's email.

        Args:
            instance (Profile): The profile instance being updated.
            validated_data (dict): The validated data for updating the profile.

        Returns:
            Profile: The updated profile instance.
        """
        owner_data = validated_data.pop('owner', {})
        email = owner_data.get('email')
        if email:
            instance.owner.email = email
            instance.owner.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'name', 'bio', 
            'created_at', 'updated_at', 'profile_image',
            'cover_image', 'blogs_count', 'workouts_count',
            'following_id', 'following_count', 'followers_count',
            'email', 'display_name'
        ]
