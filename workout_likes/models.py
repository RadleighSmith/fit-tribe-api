from django.db import models
from django.contrib.auth.models import User
from workouts.models import Workout


class WorkoutLike(models.Model):
    """
    Represents a 'like' on a workout by a user.

    Attributes:
        owner (ForeignKey): The user who liked the workout.
            ForeignKey links to User model.
        workout (ForeignKey): The workout that was liked.
            ForeignKey links to Workout model.
        created_at (DateTimeField): The date and time when the like was created

    Meta:
        ordering (list): Orders workout likes by creation date in
                        descending order.
        unique_together (tuple): Ensures that a user can like a specific
                                workout only once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(
        Workout, related_name='workout_likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = (('owner', 'workout'),)

    def __str__(self):
        return f'{self.owner.username} likes {self.workout.title}'
