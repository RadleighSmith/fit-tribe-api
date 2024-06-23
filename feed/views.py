from rest_framework import generics, permissions
from django.db.models import Count
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from followers.models import Follower

class FeedList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        user = self.request.user
        followed_users = Follower.objects.filter(owner=user).values_list('followed', flat=True)
        
        queryset = Blog.objects.filter(owner__in=followed_users).annotate(
            blog_likes_count=Count('blog_likes', distinct=True),
            blog_comments_count=Count('blogcomment', distinct=True)
        ).order_by('-created_at')
        return queryset
