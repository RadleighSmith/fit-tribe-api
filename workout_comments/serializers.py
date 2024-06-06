from rest_framework import serializers
from .models import WorkoutComment

class WorkoutCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = WorkoutComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'workout', 'comment', 
            'created_at', 'updated_at'
        ]
        
class WorkoutCommentDetailSerializer(WorkoutCommentSerializer):
    workout = serializers.ReadOnlyField(source='workout.id')