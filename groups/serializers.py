from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.

    This serializer handles the serialization and deserialization of Group objects,
    including validation and transformation of data for API representation.

    Attributes:
        id (ReadOnlyField): The unique identifier of the group.
        name (CharField): The name of the group.
        members (PrimaryKeyRelatedField): The users who are members of the group.
        description (TextField): A description of the group.
        updated_at (DateTimeField): The date and time when the group was last updated.
        created_at (DateTimeField): The date and time when the group was created.
        banner (ImageField): An optional banner image for the group with a default image.
        group_logo (ImageField): An optional logo image for the group with a default image.
    """
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)
    
    def validate_banner(self, value):
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

    def validate_group_logo(self, value):
        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 600
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

    class Meta:
        model = Group
        fields = ['id', 'name', 'members', 'description', 'updated_at', 'created_at', 'banner', 'group_logo']
