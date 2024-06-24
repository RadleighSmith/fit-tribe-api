from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group, Membership


class MembershipSerializer(serializers.ModelSerializer):
    """
    Serializer for the Membership model, which includes details of users
    who joined a group.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Membership
        fields = ['id', 'user', 'joined_at']


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model, including a list of members and their
    memberships.

    This serializer validates the banner and group logo images to ensure
    they meet the specified size and dimension requirements.
    """
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False
    )
    memberships = MembershipSerializer(
        source='membership_set', many=True, read_only=True
    )

    def validate_banner(self, value):
        """
        Validate the banner image to ensure it meets the size and
        dimension requirements.

        Args:
            value (ImageField): The banner image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB
            or if the image dimensions are not within the required range.

        Returns:
            ImageField: The validated banner image.
        """
        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 1200
        min_height = 400

        if value.size > max_size:
            raise serializers.ValidationError(
                'Image size is larger than 2 MB, please try uploading '
                'a smaller image.'
            )

        if value.image.width > max_width:
            raise serializers.ValidationError(
                f'Image width is larger than {max_width} pixels, please '
                'upload a smaller image.'
            )
        if value.image.height > max_height:
            raise serializers.ValidationError(
                f'Image height is larger than {max_height} pixels, '
                'please upload a smaller image.'
            )
        if value.image.width < min_width:
            raise serializers.ValidationError(
                f'Image width is smaller than {min_width} pixels, '
                'please upload a larger image.'
            )
        if value.image.height < min_height:
            raise serializers.ValidationError(
                f'Image height is smaller than {min_height} pixels, '
                'please upload a larger image.'
            )
        return value

    def validate_group_logo(self, value):
        """
        Validate the group logo image to ensure it meets the size and
        dimension requirements.

        Args:
            value (ImageField): The group logo image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB
            or if the image dimensions are not within the required range.

        Returns:
            ImageField: The validated group logo image.
        """
        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 600
        min_height = 400

        if value.size > max_size:
            raise serializers.ValidationError(
                'Image size is larger than 2 MB, please try uploading '
                'a smaller image.'
            )

        if value.image.width > max_width:
            raise serializers.ValidationError(
                f'Image width is larger than {max_width} pixels, please '
                'upload a smaller image.'
            )
        if value.image.height > max_height:
            raise serializers.ValidationError(
                f'Image height is larger than {max_height} pixels, '
                'please upload a smaller image.'
            )
        if value.image.width < min_width:
            raise serializers.ValidationError(
                f'Image width is smaller than {min_width} pixels, please '
                'upload a larger image.'
            )
        if value.image.height < min_height:
            raise serializers.ValidationError(
                f'Image height is smaller than {min_height} pixels, please '
                'upload a larger image.'
            )
        return value

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'description', 'updated_at', 'created_at',
            'banner', 'group_logo', 'members', 'memberships'
        ]
