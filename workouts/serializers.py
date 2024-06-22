from rest_framework import serializers
from .models import Workout, WorkoutItem
from workout_likes.models import WorkoutLike

class WorkoutItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkoutItem model.
    """
    class Meta:
        model = WorkoutItem
        fields = ['id', 'exercise_name', 'quantity']

class WorkoutSerializer(serializers.ModelSerializer):
    """
    Serializer for the Workout model.

    This serializer handles the serialization and deserialization of Workout objects,
    including additional computed fields for ownership, profile information, like status,
    and associated workout items.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    workout_items = WorkoutItemSerializer(many=True)
    workout_like_id = serializers.SerializerMethodField()
    workout_likes_count = serializers.ReadOnlyField()
    workout_comments_count = serializers.ReadOnlyField()

    def validate_banner(self, value):
        """
        Validate the banner image to ensure it meets size and dimension constraints.
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
        Validate the content image to ensure it meets size and dimension constraints.
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
        Check if the request user is the owner of the workout.
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_workout_like_id(self, obj):
        """
        Get the like ID if the workout is liked by the current user.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = WorkoutLike.objects.filter(owner=user, workout=obj).first()
            return like.id if like else None
        return None

    def create(self, validated_data):
        """
        Create a new workout instance with nested workout items.
        """
        workout_items_data = self.initial_data.get('workout_items')
        workout = Workout.objects.create(**validated_data)
        for item_data in workout_items_data:
            WorkoutItem.objects.create(workout=workout, **item_data)
        return workout

    def update(self, instance, validated_data):
        """
        Update an existing workout instance with nested workout items.
        """
        workout_items_data = self.initial_data.get('workout_items')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.banner = validated_data.get('banner', instance.banner)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        instance.workout_items.all().delete()
        for item_data in workout_items_data:
            WorkoutItem.objects.create(workout=instance, **item_data)
        return instance

    class Meta:
        model = Workout
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 
            'profile_image', 'title', 'content', 
            'created_at', 'updated_at', 'banner', 
            'image', 'workout_items', 'workout_like_id',
            'workout_likes_count', 'workout_comments_count'
        ]
