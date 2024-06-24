from django.urls import path
from workout_comments import views

urlpatterns = [
    path('workout-comments/', views.WorkoutCommentList.as_view()),
    path('workout-comments/<int:pk>/', views.WorkoutCommentDetail.as_view())
]
