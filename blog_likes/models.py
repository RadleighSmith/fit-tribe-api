from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


class BlogLike(models.Model):
    """
    Represents a like on a blog post by a user.

    Attributes:
        owner (ForeignKey): The user who liked the blog post.
            ForeignKey links to User model.
        blog (ForeignKey): The blog post that was liked.
            ForeignKey links to Blog model.
        created_at (DateTimeField): When the like was created.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='blog_likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = (('owner', 'blog'),)

    def __str__(self):
        return f'{self.owner.username} likes {self.blog.title}'
