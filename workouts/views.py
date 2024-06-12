from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Workout
from .serializers import WorkoutSerializer
from ft_api.permissions import IsOwnerOrReadOnly

class WorkoutList(generics.ListCreateAPIView):
    """
    API view to retrieve list of workouts or create a new workout.

    - GET: Returns a list of all workouts.
    - POST: Creates a new workout.
    """
    queryset = Workout.objects.annotate(
        workout_likes_count=Count('workout_likes', distinct=True),
        workout_comments_count=Count('workoutcomment', distinct=True)
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
        'workout_likes_count',
        'workout_comments_count',
        'workout_likes__created_at',
    ]
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associates the current user with the workout being created.
        """
        serializer.save(owner=self.request.user)


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a workout.

    - GET: Retrieve details of a specific workout.
    - PUT: Update the details of a specific workout.
    - DELETE: Delete a specific workout.
    """
    queryset = Workout.objects.annotate(
        workout_likes_count=Count('workout_likes', distinct=True),
        workout_comments_count=Count('workoutcomment', distinct=True)
    )
    serializer_class = WorkoutSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        """
        Retrieves the specific workout object, checking for permissions.
        """
        workout = super().get_object()
        self.check_object_permissions(self.request, workout)
        return workout
