from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from ft_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    API view to retrieve list of profiles.
    """
    queryset = Profile.objects.annotate(
        blogs_count=Count('owner__blog', distinct=True),
        workouts_count=Count('owner__workout', distinct=True),
        following_count=Count('owner__following', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'blogs_count',
        'workouts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]

    def get_serializer_context(self):
        """
        Adds the request context to the serializer context.
        """
        return {'request': self.request}


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a profile.

    - GET: Retrieve details of a specific profile.
    - PUT: Update the details of a specific profile (only allowed if the user
      is the owner).
    - DELETE: Delete the profile and the associated user.
    """
    queryset = Profile.objects.annotate(
        blogs_count=Count('owner__blog', distinct=True),
        workouts_count=Count('owner__workout', distinct=True),
        following_count=Count('owner__following', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        """
        Adds the request context to the serializer context.
        """
        return {'request': self.request}

    def delete(self, request, *args, **kwargs):
        """
        Handle deletion of the profile and the associated user.
        """
        profile = self.get_object()
        user = profile.owner
        profile.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
