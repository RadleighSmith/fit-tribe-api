from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Represents a follower relationship between two users.

    Attributes:
        owner (ForeignKey): The user who is following another user.
            ForeignKey links to the User model.
        followed (ForeignKey): The user who is being followed.
            ForeignKey links to the User model.
        created_at (DateTimeField): The date and time when the follow
            relationship was created.

    Meta:
        ordering (list): Orders follower records by creation date in
            descending order.
        unique_together (tuple): Ensures that a follower-followed
            relationship is unique.
        verbose_name (str): Adds readable name for the model in singular form.
        verbose_name_plural (str): Adds readable name for the model in plural
            form.

    Methods:
        __str__(): Returns a string representation of the follower
            relationship.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE,
        verbose_name='follower'
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE,
        verbose_name='followed'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'followed')
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

    def __str__(self):
        return f'{self.owner.username} follows {self.followed.username}'
