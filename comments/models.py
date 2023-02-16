from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review
# Create your models here.

# Credit CI walkthrough


class Comment(models.Model):
    """
    Allows user to put comments on a Review post
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    comment_text = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment_text
