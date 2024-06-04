from rest_framework import serializers
from .models import BlogComment

class BlogCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = BlogComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'blog', 'comment', 
            'created_at', 'updated_at'
        ]

class BlogCommentDetailSerializer(BlogCommentSerializer):
    blog = serializers.ReadOnlyField(source='blog.id')