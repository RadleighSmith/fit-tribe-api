from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from ft_api.permissions import IsOwnerOrReadOnly
from .models import BlogComment
from .serializers import BlogCommentSerializer, BlogCommentDetailSerializer


class BlogCommentList(generics.ListCreateAPIView):
    """
    API view to retrieve list of blog comments or create a new comment.

    - GET: Returns a list of all comments for a specific blog.
    - POST: Creates a new comment for a blog.
    """
    serializer_class = BlogCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = BlogComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog']

    def perform_create(self, serializer):
        """
        Associates the current user with the comment being created.
        """
        serializer.save(owner=self.request.user)


class BlogCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a blog comment.

    - GET: Retrieve details of a specific comment.
    - PUT: Update the details of a specific comment.
    - DELETE: Delete a specific comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogCommentDetailSerializer
    queryset = BlogComment.objects.all()
