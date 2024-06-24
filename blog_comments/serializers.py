from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import BlogComment


class BlogCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogComment model.

    This serializer handles the serialization and deserialization of
    BlogComment objects, including additional computed fields for ownership,
    profile information, and timestamps.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url'
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of this comment.

        Args:
            obj (BlogComment): The comment object being serialized.

        Returns:
            bool: True if the current user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Get the natural time format of the comment's creation time.

        Args:
            obj (BlogComment): The comment object being serialized.

        Returns:
            str: The natural time format of the comment's creation time.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Get the natural time format of the comment's last update time.

        Args:
            obj (BlogComment): The comment object being serialized.

        Returns:
            str: The natural time format of the comment's last update time.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = BlogComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'blog', 'comment',
            'created_at', 'updated_at'
        ]


class BlogCommentDetailSerializer(BlogCommentSerializer):
    """
    Detailed serializer for the BlogComment model with read-only blog field.
    """
    blog = serializers.ReadOnlyField(source='blog.id')
