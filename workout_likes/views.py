from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from workout_likes.models import WorkoutLike
from workout_likes.serializers import WorkoutLikeSerializer

class WorkoutLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkoutLikeSerializer
    queryset = WorkoutLike.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class WorkoutLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkoutLikeSerializer
    queryset = WorkoutLike.objects.all()