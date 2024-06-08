from rest_framework import generics, permissions
from .models import Group
from .serializers import GroupSerializer
from ft_api.permissions import IsAdminOrReadOnly  # Import the custom permission

class GroupList(generics.ListCreateAPIView):
    """
    API view to retrieve list of groups or create a new group.

    - GET: Returns a list of all groups.
    - POST: Allows an admin user to create a new group.

    The perform_create method associates the current logged-in user with the group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a group.

    - GET: Retrieve details of a specific group.
    - PUT: Update the details of a specific group (only allowed if the user is an admin).
    - DELETE: Delete a specific group (only allowed if the user is an admin).

    Update operation is allowed to modify the group's details.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]