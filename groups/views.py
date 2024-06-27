from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db import IntegrityError, DatabaseError
from .models import Group, Membership
from .serializers import GroupSerializer, MembershipSerializer
from ft_api.permissions import IsAdminOrReadOnly


class GroupList(generics.ListCreateAPIView):
    """
    API view to retrieve list of groups or create a new group.

    - GET: Returns a list of all groups.
    - POST: Allows an admin user to create a new group.
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
    - PUT: Update the details of a specific group (only allowed if
      the user is an admin).
    - DELETE: Delete a specific group (only allowed if the user is
      an admin).
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_update(self, serializer):
        serializer.validated_data.pop('members', None)
        serializer.save()


class JoinGroup(generics.GenericAPIView):
    """
    API view to join a group.

    - POST: Adds the current user to the group members.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()

    def post(self, request, pk):
        try:
            group = self.get_object()
            Membership.objects.create(user=request.user, group=group)
            return Response({'status': 'joined'}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response(
                {'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND
            )
        except IntegrityError:
            return Response(
                {'error': 'Already a member of this group'},
                status=status.HTTP_400_BAD_REQUEST
            )


class LeaveGroup(generics.GenericAPIView):
    """
    API view to leave a group.

    - POST: Removes the current user from the group members.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()

    def post(self, request, pk):
        try:
            group = self.get_object()
            membership = Membership.objects.get(user=request.user, group=group)
            membership.delete()
            return Response({'status': 'left'}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response(
                {'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND
            )
        except Membership.DoesNotExist:
            return Response(
                {'error': 'Not a member of this group'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except DatabaseError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MembershipList(generics.ListAPIView):
    """
    API view to list memberships of the current user.

    - GET: Returns a list of memberships for the current user.
    """
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user)
