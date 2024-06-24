from django.db import IntegrityError
from rest_framework import serializers
from workout_likes.models import WorkoutLike


class WorkoutLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkoutLike model.

    This serializer handles the serialization and deserialization of
    WorkoutLike objects, including validation to prevent duplicate likes.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WorkoutLike
        fields = ['id', 'owner', 'workout', 'created_at']

    def create(self, validated_data):
        """
        Creates a new WorkoutLike instance, ensuring no duplicates.

        Args:
            validated_data (dict): The validated data for creating a
                                WorkoutLike.

        Raises:
            serializers.ValidationError: If a duplicate like is detected.

        Returns:
            WorkoutLike: The created WorkoutLike instance.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'This like already exists.'
            })
