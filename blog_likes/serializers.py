from django.db import IntegrityError
from rest_framework import serializers
from blog_likes.models import BlogLike

class BlogLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta: 
        model = BlogLike
        fields = ['id', 'owner', 'blog', 'created_at']
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })