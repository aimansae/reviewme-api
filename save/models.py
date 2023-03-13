from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review


class Save(models.Model):
    '''
    Model to save a review regarding a certain product
    '''

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-created_at']
        unique_together = ('owner', 'review')

    def __str__(self):
        return f'{self.owner} saved {self.review}'
