from rest_framework import serializers
from .models import Workout, WorkoutItem

class WorkoutItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutItem
        fields = ['id', 'exercise_name', 'quantity']

class WorkoutSerializer(serializers.ModelSerializer):
    workout_items = WorkoutItemSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at', 'banner', 'image', 'workout_items']

    def create(self, validated_data):
        workout_items_data = validated_data.pop('workout_items')
        workout = Workout.objects.create(**validated_data)
        for item_data in workout_items_data:
            WorkoutItem.objects.create(workout=workout, **item_data)
        return workout

    def update(self, instance, validated_data):
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
