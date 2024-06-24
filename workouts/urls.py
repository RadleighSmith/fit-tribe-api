from django.urls import path
from .views import WorkoutList, WorkoutDetail

urlpatterns = [
    path('workouts/', WorkoutList.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetail.as_view(), name='workout-detail'),
]
