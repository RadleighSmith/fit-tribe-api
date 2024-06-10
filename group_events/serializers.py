from rest_framework import serializers
from .models import GroupEvent

class GroupEventSerializer(serializers.ModelSerializer):
    """
    Serializer for the GroupEvent model.
    """
    def validate_banner(self, value):
        """
        Validate the banner image to ensure it meets the size and dimension requirements.
        """
        if value is None:
            return value  # Allow no image to be provided.

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

    class Meta:
        model = GroupEvent
        fields = [
            'id', 'group', 'name', 'description', 'location', 
            'start_time', 'end_time', 'banner', 'created_at', 
            'updated_at'
        ]
    
    
