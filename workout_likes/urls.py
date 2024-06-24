from django.urls import path
from workout_likes import views

urlpatterns = [
    path('workout-likes/', views.WorkoutLikeList.as_view()),
    path('workout-likes/<int:pk>/', views.WorkoutLikeDetail.as_view()),
]
