from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    """
    Represents a workout session created by a user.

    Attributes:
        owner (ForeignKey): The user who owns the workout.
        title (CharField): The title of the workout.
        content (TextField): Detailed description of the workout.
        created_at (DateTimeField): Timestamp when the workout was created.
        updated_at (DateTimeField): Timestamp when the workout was last updated
        banner (ImageField): Optional banner image for the workout.
        image (ImageField): Optional content image for the workout.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(
        upload_to='workout_banners/',
        default='../default_workout_banner_sd3cfj'
    )
    image = models.ImageField(
        upload_to='workout_images/',
        default='../default_post_eznpr6',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


class WorkoutItem(models.Model):
    """
    Represents an individual exercise in a workout session.

    Attributes:
        workout (ForeignKey): The workout this item belongs to.
        exercise_name (CharField): The name of the exercise.
        quantity (IntegerField): The quantity or repetitions of the exercise.
    """
    workout = models.ForeignKey(
        Workout, related_name='workout_items', on_delete=models.CASCADE
    )
    exercise_name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.exercise_name} - {self.quantity}'
