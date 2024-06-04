from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from blog_likes.models import BlogLike
from blog_likes.serializers import BlogLikeSerializer


class BlogLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogLikeSerializer
    queryset = BlogLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogLikeSerializer
    queryset = BlogLike.objects.all()