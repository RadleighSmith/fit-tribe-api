from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer handles the serialization and deserialization of Profile objects,
    including additional computed fields for ownership, blog count, workout count,
    following status, follower counts, group count, and group names.

    Attributes:
        owner (ReadOnlyField): The username of the profile owner.
        is_owner (SerializerMethodField): Indicates if the requesting user is the owner of the profile.
        blogs_count (ReadOnlyField): The number of blogs created by the profile owner.
        workouts_count (ReadOnlyField): The number of workouts created by the profile owner.
        following_id (SerializerMethodField): The ID of the following relationship if the requesting user follows the profile owner.
        following_count (ReadOnlyField): The number of users the profile owner is following.
        followers_count (ReadOnlyField): The number of users following the profile owner.
        email (ReadOnlyField): The email of the profile owner.
        display_name (BooleanField): Indicates if the real name should be displayed on the profile.

    Methods:
        get_is_owner(obj): Checks if the requesting user is the owner of the profile.
        get_following_id(obj): Gets the ID of the following relationship if the requesting user follows the profile owner.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    is_owner = serializers.SerializerMethodField()
    blogs_count = serializers.ReadOnlyField()
    workouts_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    display_name = serializers.BooleanField(default=False)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'name', 'bio', 
            'created_at', 'updated_at', 'profile_image',
            'cover_image', 'blogs_count', 'workouts_count',
            'following_id', 'following_count', 'followers_count',
            'email', 'display_name'
        ]
