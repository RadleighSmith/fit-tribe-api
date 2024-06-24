from rest_framework import generics, permissions
from django.db.models import Count
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from followers.models import Follower


class FeedList(generics.ListAPIView):
    """
    API view to retrieve a list of blog posts from followed users.

    This view returns a list of blog posts created by users that the
    current user follows. The posts are annotated with counts for
    likes and comments, and ordered by creation date in descending order.

    Permission:
    - The user must be authenticated to access this view.

    Methods:
        get_queryset(self): Retrieves the queryset of blog posts created by
        followed users.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        """
        Retrieves the queryset of blog posts created by followed users.

        This method filters the blog posts to include only those created
        by users that the current user follows. The posts are annotated
        with counts for likes and comments, and ordered by creation date
        in descending order.

        Returns:
            QuerySet: The queryset of filtered blog posts.
        """
        user = self.request.user
        followed_users = Follower.objects.filter(
            owner=user
        ).values_list('followed', flat=True)

        queryset = Blog.objects.filter(
            owner__in=followed_users
        ).annotate(
            blog_likes_count=Count('blog_likes', distinct=True),
            blog_comments_count=Count('blogcomment', distinct=True)
        ).order_by('-created_at')

        return queryset
