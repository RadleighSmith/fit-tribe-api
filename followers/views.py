from rest_framework import generics, permissions
from ft_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    API view to retrieve list of followers or create a new follower
    relationship.

    - GET: Returns a list of all follower relationships.
    - POST: Allows a logged-in user to follow another user by creating a
      follower relationship.

    The perform_create method associates the current logged-in user with the
    follower relationship.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a follower relationship.

    - GET: Retrieve details of a specific follower relationship.
    - DELETE: Allows the owner of the follower relationship to unfollow a user
      by deleting the relationship.

    Update operation is not allowed, as the action is either to follow or
    unfollow a user.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
