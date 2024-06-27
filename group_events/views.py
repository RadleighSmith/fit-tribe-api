from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import GroupEvent, EventMembership
from .serializers import GroupEventSerializer, EventMembershipSerializer
from ft_api.permissions import IsAdminOrReadOnly


class GroupEventList(generics.ListCreateAPIView):
    """
    API view to retrieve list of group events or create a new group event.

    - GET: Returns a list of all group events.
    - POST: Allows an admin user to create a new group event.
    """
    serializer_class = GroupEventSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        group_id = self.request.query_params.get('group_id', None)
        if group_id:
            return GroupEvent.objects.filter(group_id=group_id)
        return GroupEvent.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class GroupEventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a group event.

    - GET: Retrieve details of a specific group event.
    - PUT: Update the details of a specific group event (only allowed if
           the user is an admin).
    - DELETE: Delete a specific group event (only allowed if the user is
              an admin).
    """
    queryset = GroupEvent.objects.all()
    serializer_class = GroupEventSerializer
    permission_classes = [IsAdminOrReadOnly]


class JoinEvent(generics.GenericAPIView):
    """
    API view to join a group event.

    - POST: Adds the current user to the event members.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventMembershipSerializer

    def post(self, request, pk):
        try:
            event = GroupEvent.objects.get(pk=pk)
            if EventMembership.objects.filter(
                user=request.user, event=event
            ).exists():
                return Response(
                    {'error': 'Already joined this event.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            EventMembership.objects.create(user=request.user, event=event)
            return Response({'status': 'joined'}, status=status.HTTP_200_OK)
        except GroupEvent.DoesNotExist:
            return Response(
                {'error': 'Event not found.'},
                status=status.HTTP_404_NOT_FOUND
            )


class LeaveEvent(generics.GenericAPIView):
    """
    API view to leave a group event.

    - POST: Removes the current user from the event members.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventMembershipSerializer

    def post(self, request, pk):
        try:
            event = GroupEvent.objects.get(pk=pk)
            membership = EventMembership.objects.get(
                user=request.user, event=event
            )
            membership.delete()
            return Response({'status': 'left'}, status=status.HTTP_200_OK)
        except GroupEvent.DoesNotExist:
            return Response(
                {'error': 'Event not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except EventMembership.DoesNotExist:
            return Response(
                {'error': 'Not a member of this event.'},
                status=status.HTTP_400_BAD_REQUEST
            )
