from django.db import IntegrityError
from rest_framework import serializers
from blog_likes.models import BlogLike


class BlogLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogLike model.

    This serializer handles the serialization and deserialization of
    BlogLike objects, ensuring that the owner field is read-only and
    providing custom validation to handle potential duplicate entries.

    Attributes:
        owner (ReadOnlyField): The username of the user who liked the
        blog post.

    Methods:
        create(validated_data): Custom create method to handle
        IntegrityError and provide a user-friendly error message.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlogLike
        fields = ['id', 'owner', 'blog', 'created_at']

    def create(self, validated_data):
        """
        Create a new BlogLike instance.

        Args:
            validated_data (dict): The validated data for creating the
            BlogLike instance.

        Returns:
            BlogLike: The created BlogLike instance.

        Raises:
            serializers.ValidationError: If a duplicate BlogLike entry
            is detected.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplicate'
            })
