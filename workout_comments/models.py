from django.db import models
from django.contrib.auth.models import User
from workouts.models import Workout


class WorkoutComment(models.Model):
    """
    Model representing a comment on a workout.

    Attributes:
        owner (ForeignKey): The user who owns the comment.
        workout (ForeignKey): The workout the comment is related to.
        comment (TextField): The content of the comment.
        created_at (DateTimeField): The date and time when the comment
        was created.
        updated_at (DateTimeField): The date and time when the comment
        was last updated.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
