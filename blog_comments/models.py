from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


class BlogComment(models.Model):
    """
    Represents a comment made by a user on a blog post.

    Attributes:
        owner (ForeignKey): The user who made the comment. ForeignKey
            links to User model.
        blog (ForeignKey): The blog post that the comment is related to.
            ForeignKey links to Blog model.
        comment (TextField): The content of the comment.
        created_at (DateTimeField): The date and time when the comment
            was created.
        updated_at (DateTimeField): The date and time when the comment
            was last updated.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
