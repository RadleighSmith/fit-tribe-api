from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from followers.models import Follower

class FeedList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        # Get the list of users the current user is following
        user = self.request.user
        followed_users = Follower.objects.filter(owner=user).values_list('followed', flat=True)

        # Filter blog posts from followed users
        queryset = Blog.objects.filter(owner__in=followed_users).order_by('-created_at')
        return queryset
