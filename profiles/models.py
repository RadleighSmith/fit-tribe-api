from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Profile model to store additional information for each user.

    Attributes:
        owner (OneToOneField): The user that this profile belongs to.
        name (CharField): The real name of the user.
        bio (TextField): A short bio about the user.
        created_at (DateTimeField): The date and time when the profile was created.
        updated_at (DateTimeField): The date and time when the profile was last updated.
        profile_image (ImageField): The profile image of the user.
        cover_image (ImageField): The cover image for the user's profile.
        display_name (BooleanField): Whether to display the real name on the profile.

    Methods:
        __str__(): Returns a string representation of the profile.
    """
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
    display_name = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Profile Page"

def create_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile object whenever a new User is created.

    Args:
        sender: The model class sending the signal.
        instance: The instance of the model that just got created.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
