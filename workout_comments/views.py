from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from .models import WorkoutComment
from .serializers import WorkoutCommentSerializer, WorkoutCommentDetailSerializer

class WorkoutCommentList(generics.ListCreateAPIView):
    serializer_class = WorkoutCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutComment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class WorkoutCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkoutCommentDetailSerializer
    queryset = WorkoutComment.objects.all()
    