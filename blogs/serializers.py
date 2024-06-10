from rest_framework import serializers
from .models import Blog
from blog_likes.models import BlogLike

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model.

    This serializer handles the serialization and deserialization of Blog objects,
    including additional computed fields for ownership, profile information, and like status.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    like_id = serializers.SerializerMethodField()

    def validate_banner(self, value):
        """
        Validate the banner image to ensure it meets the size and dimension requirements.

        Args:
            value (ImageField): The banner image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB or if the image dimensions are not within the required range.

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

    def validate_image(self, value):
        """
        Validate the content image to ensure it meets the size and dimension requirements.

        Args:
            value (ImageField): The content image to be validated.

        Raises:
            serializers.ValidationError: If the image size exceeds 2 MB or if the image dimensions are not within the required range.

        Returns:
            ImageField: The validated content image.
        """
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

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of this blog post.

        Args:
            obj (Blog): The blog object being serialized.

        Returns:
            bool: True if the current user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        """
        Get the ID of the 'BlogLike' instance if the current user has liked the given blog.

        Args:
            obj (Blog): The blog object being serialized.

        Returns:
            int or None: The ID of the 'BlogLike' instance if the current user has liked the blog,
                         None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = BlogLike.objects.filter(owner=user, blog=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Blog
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 
            'profile_image', 'title', 'content', 
            'created_at', 'updated_at', 'banner', 
            'image', 'like_id'
        ]
