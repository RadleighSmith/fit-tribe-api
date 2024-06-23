from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from ft_api.permissions import IsOwnerOrReadOnly
from .models import BlogComment
from .serializers import BlogCommentSerializer, BlogCommentDetailSerializer

class BlogCommentList(generics.ListCreateAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = BlogComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class BlogCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogCommentDetailSerializer
    queryset = BlogComment.objects.all()