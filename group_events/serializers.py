from rest_framework import serializers
from .models import GroupEvent, EventMembership


class EventMembershipSerializer(serializers.ModelSerializer):
    """
    Serializer for the EventMembership model.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = EventMembership
        fields = ['id', 'user', 'joined_at']


class GroupEventSerializer(serializers.ModelSerializer):
    """
    Serializer for the GroupEvent model.
    """
    memberships = EventMembershipSerializer(
        source='eventmembership_set', many=True, read_only=True
    )
    is_joined = serializers.SerializerMethodField()

    def get_is_joined(self, obj):
        """
        Determine if the current user is a member of the event.

        Args:
            obj (GroupEvent): The event object being serialized.

        Returns:
            bool: True if the current user is a member of the event,
                  False otherwise.
        """
        request = self.context.get('request', None)
        if request is not None and request.user.is_authenticated:
            return EventMembership.objects.filter(
                user=request.user, event=obj
            ).exists()
        return False

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
        if value is None:
            return value

        max_size = 1024 * 1024 * 2  # 2 MB
        max_width = 4096
        max_height = 4096
        min_width = 1200
        min_height = 400

        if value.size > max_size:
            raise serializers.ValidationError(
                'Image size is larger than 2 MB.'
            )
        if value.image.width > max_width or value.image.width < min_width:
            raise serializers.ValidationError(
                f'Image width must be between {min_width} and {max_width} '
                f'pixels.'
            )
        if value.image.height > max_height or value.image.height < min_height:
            raise serializers.ValidationError(
                f'Image height must be between {min_height} and {max_height} '
                f'pixels.'
            )
        return value

    class Meta:
        model = GroupEvent
        fields = [
            'id', 'group', 'name', 'description', 'location', 'start_time',
            'end_time', 'banner', 'created_at', 'updated_at', 'memberships',
            'is_joined'
        ]
