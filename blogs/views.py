from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Blog
from .serializers import BlogSerializer
from ft_api.permissions import IsOwnerOrReadOnly

class BlogList(generics.ListCreateAPIView):
    """
    API view to retrieve list of blogs or create a new blog.

    - GET: Returns a list of all blogs.
    - POST: Creates a new blog.
    """
    queryset = Blog.objects.annotate(
        blog_likes_count=Count('blog_likes', distinct=True),
        blog_comments_count=Count('blogcomment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'blog_likes_count',
        'blog_comments_count',
        'likes__created_at',
    ]
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associates the current user with the blog being created.
        """
        serializer.save(owner=self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a blog.

    - GET: Retrieve details of a specific blog.
    - PUT: Update the details of a specific blog.
    - DELETE: Delete a specific blog.
    """
    queryset = Blog.objects.annotate(
        blog_likes_count=Count('blog_likes', distinct=True),
        blog_comments_count=Count('blogcomment', distinct=True)
    )
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        """
        Retrieves the specific blog object, checking for permissions.
        """
        blog = super().get_object()
        self.check_object_permissions(self.request, blog)
        return blog
