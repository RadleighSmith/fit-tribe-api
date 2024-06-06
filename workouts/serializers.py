from rest_framework import serializers
from .models import Workout, WorkoutItem

class WorkoutItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutItem
        fields = ['id', 'exercise_name', 'quantity']

class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    workout_items = WorkoutItemSerializer(many=True)

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
        Validates the content image to ensure it meets size and dimension constraints.
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
        Checks if the requesting user is the owner of the workout post.
        """
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        """
        Creates a new workout post with associated workout items.
        """
        workout_items_data = validated_data.pop('workout_items')
        workout = Workout.objects.create(**validated_data)
        for item_data in workout_items_data:
            WorkoutItem.objects.create(workout=workout, **item_data)
        return workout

    def update(self, instance, validated_data):
        """
        Updates an existing workout and its associated workout items.
        """
        workout_items_data = validated_data.pop('workout_items')
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
            'image', 'workout_items'
        ]
