from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(
        upload_to='workout_banners/', default='../default_workout_banner_sd3cfj'
    )
    image = models.ImageField(
        upload_to='workout_images/', default='../default_post_eznpr6', 
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.id} {self.title}'

class WorkoutItem(models.Model):
    workout = models.ForeignKey(Workout, related_name='workout_items', on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.exercise_name} - {self.quantity}'
