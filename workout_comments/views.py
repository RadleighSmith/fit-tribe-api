from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from ft_api.permissions import IsOwnerOrReadOnly
from .models import WorkoutComment
from .serializers import (
    WorkoutCommentSerializer,
    WorkoutCommentDetailSerializer
)


class WorkoutCommentList(generics.ListCreateAPIView):
    """
    API view to retrieve list of workout comments or create a new comment.

    - GET: Returns a list of all workout comments.
    - POST: Allows a logged-in user to create a new workout comment.
    """
    serializer_class = WorkoutCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['workout']

    def perform_create(self, serializer):
        """
        Save the new workout comment with the owner set to the current user.
        """
        serializer.save(owner=self.request.user)


class WorkoutCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a workout comment.

    - GET: Retrieve details of a specific workout comment.
    - PUT: Update the details of a specific workout comment.
    - DELETE: Delete a specific workout comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkoutCommentDetailSerializer
    queryset = WorkoutComment.objects.all()
