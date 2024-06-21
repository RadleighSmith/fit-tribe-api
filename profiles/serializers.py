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
        validate_profile_image(value): Validates the profile image.
        validate_cover_image(value): Validates the cover image.
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

    def validate_profile_image(self, value):
        """
        Validate the profile image to ensure it meets the size and dimension requirements.

        Args:
            value (ImageField): The profile image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB or if the image dimensions are not within the required range.

        Returns:
            ImageField: The validated profile image.
        """
        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 200
        min_height = 200
        
        if value.size > max_size:
            raise serializers.ValidationError(
                'Image size is larger than 2 MB, please try uploading a smaller image.'
            )

        if value.image.width > max_width:
            raise serializers.ValidationError(
                f'Image width is larger than {max_width} pixels, please upload a smaller image.'
            )
        if value.image.height > max_height:
            raise serializers.ValidationError(
                f'Image height is larger than {max_height} pixels, please upload a smaller image.'
            )
        if value.image.width < min_width:
            raise serializers.ValidationError(
                f'Image width is smaller than {min_width} pixels, please upload a larger image.'
            )
        if value.image.height < min_height:
            raise serializers.ValidationError(
                f'Image height is smaller than {min_height} pixels, please upload a larger image.'
            )
        return value

    def validate_cover_image(self, value):
        """
        Validate the cover image to ensure it meets the size and dimension requirements.

        Args:
            value (ImageField): The cover image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB or if the image dimensions are not within the required range.

        Returns:
            ImageField: The validated cover image.
        """
        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 1200
        min_height = 400
        
        if value.size > max_size:
            raise serializers.ValidationError(
                'Image size is larger than 2 MB, please try uploading a smaller image.'
            )

        if value.image.width > max_width:
            raise serializers.ValidationError(
                f'Image width is larger than {max_width} pixels, please upload a smaller image.'
            )
        if value.image.height > max_height:
            raise serializers.ValidationError(
                f'Image height is larger than {max_height} pixels, please upload a smaller image.'
            )
        if value.image.width < min_width:
            raise serializers.ValidationError(
                f'Image width is smaller than {min_width} pixels, please upload a larger image.'
            )
        if value.image.height < min_height:
            raise serializers.ValidationError(
                f'Image height is smaller than {min_height} pixels, please upload a larger image.'
            )
        return value

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
