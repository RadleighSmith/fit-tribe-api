from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class GroupEvent(models.Model):
    """
    Represents an event within a group that users can join.

    Attributes:
        group (ForeignKey): The parent group to which the event belongs.
        name (CharField): The name of the event.
        description (TextField): A detailed description of the event.
        location (CharField): The location where the event will take place.
        start_date (DateField): The start date of the event.
        start_time (TimeField): The start time of the event.
        end_date (DateField): The end date of the event.
        end_time (TimeField): The end time of the event.
        banner (ImageField): An optional banner image for the event.
        created_at (DateTimeField): The date and time when the event was
                                    created.
        updated_at (DateTimeField): The date and time when the event was
                                    last updated.
    """
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='events'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField(default='2024-01-01')
    start_time = models.TimeField(default='00:00:00')
    end_date = models.DateField(default='2024-01-01')
    end_time = models.TimeField(default='00:00:00')
    banner = models.ImageField(
        upload_to='event_banners/', blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', '-start_time']
        verbose_name = 'Group Event'
        verbose_name_plural = 'Group Events'

    def __str__(self):
        return f'{self.name} ({self.group.name})'


class EventMembership(models.Model):
    """
    Represents a membership of a user to a specific event.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
        ordering = ['-joined_at']

    def __str__(self):
        return f'{self.user.username} joined {self.event.name}'
