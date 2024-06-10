from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer handles the serialization and deserialization of Profile objects, 
    including additional computed fields for ownership, following status, and counts 
    of posts, followers, and followings.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

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
        Get the ID of the 'Follower' instance if the current user is following the owner of this profile.

        Args:
            obj (Profile): The profile object being serialized.

        Returns:
            int or None: The ID of the 'Follower' instance if the current user is following the owner,
                         None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, following=obj.owner).first()
            return getattr(following, 'id', None)
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'name', 'bio', 
            'created_at', 'updated_at', 'profile_image',
            'cover_image', 'following_id', 'posts_count',
            'followers_count', 'following_count',
        ]
