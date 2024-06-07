from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    """
    Represents a follower relationship between two users.

    Attributes:
        follower (ForeignKey): The user who is following another user. 
            ForeignKey links to the User model.
        following (ForeignKey): The user who is being followed.
            ForeignKey links to the User model.
        created_at (DateTimeField): The date and time when the follow relationship was created.

    Meta:
        ordering (list): Orders follower records by creation date in descending order.
        unique_together (tuple): Ensures that a follower-following relationship is unique.
        verbose_name (str): Adds readable name for the model in singular form.
        verbose_name_plural (str): Adds readable name for the model in plural form.

    Methods:
        __str__(): Returns a string representation of the follower relationship.
    """
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE, verbose_name='follower')
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE, verbose_name='following')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ('follower', 'following')
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'
        
    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
