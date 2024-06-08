from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
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
    members = models.ManyToManyField(User, through='Membership', related_name='group_memberships')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        
    def __str__(self):
        return f'{self.id} {self.name}'

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')
        
    def __str__(self):
        return f'{self.user.username} in {self.group.name}'
