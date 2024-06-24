from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from blog_likes.models import BlogLike
from blog_likes.serializers import BlogLikeSerializer


class BlogLikeList(generics.ListCreateAPIView):
    """
    API view to retrieve list of blog likes or create a new blog like.

    - GET: Returns a list of all blog likes.
    - POST: Creates a new blog like for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogLikeSerializer
    queryset = BlogLike.objects.all()

    def perform_create(self, serializer):
        """
        Associates the current logged-in user with the blog like being created.

        Args:
            serializer (BlogLikeSerializer): The serializer instance
            containing the validated data for creating the blog like.
        """
        serializer.save(owner=self.request.user)


class BlogLikeDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a blog like.

    - GET: Retrieve details of a specific blog like.
    - DELETE: Delete a specific blog like.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogLikeSerializer
    queryset = BlogLike.objects.all()
