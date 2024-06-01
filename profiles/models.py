from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
        upload_to='profile_pictures/', default='../default_profile_image_g43b7d'
    )
    cover_image = models.ImageField(
        upload_to='cover_images/', default='../default_cover_image_d23fdc'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Profile Page"