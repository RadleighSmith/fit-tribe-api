from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    Represents a group in the fitness social media site.

    Attributes:
        name (CharField): The name of the group.
        members (ManyToManyField): The users who are members of the group.
        description (TextField): A description of the group.
        updated_at (DateTimeField): The date and time when the group
        was last updated.
        created_at (DateTimeField): The date and time when the group
        was created.
        banner (ImageField): An optional banner image for the group
        with a default image.
        group_logo (ImageField): An optional logo image for the group
        with a default image.

    Meta:
        ordering (list): Orders group records by creation date in
        descending order.
        verbose_name (str): Adds readable name for the model in
        singular form.
        verbose_name_plural (str): Adds readable name for the model
        in plural form.

    Methods:
        __str__(): Returns a string representation of the group.
    """
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        User, through='Membership', related_name='group_memberships'
    )
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(
        upload_to='group_banners/', default='../default_cover_image_d23fdc'
    )
    group_logo = models.ImageField(
        upload_to='group_logos/', default='../default_post_eznpr6',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return f'{self.id} {self.name}'


class Membership(models.Model):
    """
    Represents a membership relationship between a user and a group.

    Attributes:
        user (ForeignKey): The user who is a member of the group.
        group (ForeignKey): The group the user is a member of.
        joined_at (DateTimeField): The date and time when the user
        joined the group.

    Methods:
        __str__(): Returns a string representation of the membership.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} joined {self.group.name}'
