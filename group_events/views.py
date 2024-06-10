from rest_framework import generics, permissions
from .models import GroupEvent
from .serializers import GroupEventSerializer
from ft_api.permissions import IsAdminOrReadOnly

class GroupEventList(generics.ListCreateAPIView):
    """
    API view to retrieve list of group events or create a new group event.

    - GET: Returns a list of all group events.
    - POST: Allows an admin user to create a new group event.
    """
    queryset = GroupEvent.objects.all()
    serializer_class = GroupEventSerializer
    permission_classes = [IsAdminOrReadOnly]

class GroupEventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a group event.

    - GET: Retrieve details of a specific group event.
    - PUT: Update the details of a specific group event (only allowed if the user is an admin).
    - DELETE: Delete a specific group event (only allowed if the user is an admin).
    """
    queryset = GroupEvent.objects.all()
    serializer_class = GroupEventSerializer
    permission_classes = [IsAdminOrReadOnly]