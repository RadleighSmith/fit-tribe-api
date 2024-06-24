from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from workout_likes.models import WorkoutLike
from workout_likes.serializers import WorkoutLikeSerializer


class WorkoutLikeList(generics.ListCreateAPIView):
    """
    API view to retrieve list of workout likes or create a new like.

    - GET: Returns a list of all workout likes.
    - POST: Creates a new workout like for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkoutLikeSerializer
    queryset = WorkoutLike.objects.all()

    def perform_create(self, serializer):
        """
        Associates the current user with the workout like being created.
        """
        serializer.save(owner=self.request.user)


class WorkoutLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a workout like.

    - GET: Retrieve details of a specific workout like.
    - PUT: Update the details of a specific workout like.
    - DELETE: Delete a specific workout like.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkoutLikeSerializer
    queryset = WorkoutLike.objects.all()
