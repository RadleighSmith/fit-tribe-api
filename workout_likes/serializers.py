from django.db import IntegrityError
from rest_framework import serializers
from workout_likes.models import WorkoutLike

class WorkoutLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = WorkoutLike
        fields = ['id', 'owner', 'workout', 'created_at']
        
        def create(self, validated_data):
            try:
                return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({
                    'detail': 'This like already exists.'
                })