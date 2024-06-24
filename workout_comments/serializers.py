from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import WorkoutComment


class WorkoutCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkoutComment model.

    This serializer handles the serialization and deserialization of
    WorkoutComment objects, including additional computed fields for
    ownership, profile information, and timestamps.
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
        Check if the request user is the owner of the workout comment.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Return the natural time format of the comment's creation time.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Return the natural time format of the comment's last update time.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = WorkoutComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'workout', 'comment',
            'created_at', 'updated_at'
        ]


class WorkoutCommentDetailSerializer(WorkoutCommentSerializer):
    """
    Serializer for detailed view of WorkoutComment model.

    Extends WorkoutCommentSerializer to include workout ID as a read-only
    field.
    """
    workout = serializers.ReadOnlyField(source='workout.id')
