from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workout
from .serializers import WorkoutSerializer
from ft_api.permissions import IsOwnerOrReadOnly

class WorkoutList(APIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            workout = Workout.objects.get(pk=pk)
            self.check_object_permissions(self.request, workout)
            return workout
        except Workout.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        workout = self.get_object(pk)
        serializer = WorkoutSerializer(workout, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        workout = self.get_object(pk)
        serializer = WorkoutSerializer(workout, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workout = self.get_object(pk)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
