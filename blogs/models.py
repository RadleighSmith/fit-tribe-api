from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    Represents a blog post by a user.

    Attributes:
        owner (ForeignKey): The user who owns the blog post.
            ForeignKey links to User model.
        title (CharField): The blog post's title.
        content (TextField): The blog post's content.
        created_at (DateTimeField): When the post was created.
        updated_at (DateTimeField): When the post was last updated.
        banner (ImageField): Optional banner image, with a default.
        image (ImageField): Optional content image, with a default
            set so we can always reference an image url.

    Meta:
        ordering: Blog posts are ordered by creation date, newest first.

    Methods:
        __str__(): Returns the blog post's ID and title.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(
        upload_to='blog_banners/', default='../default_blog_banner_t4cat3'
    )
    image = models.ImageField(
        upload_to='blog_images/', default='../default_post_eznpr6',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
