from django.db import models
from django.contrib.auth.models import User

# Credit C.I. DRF-API walkthrough.
# Modeification made


class Review(models.Model):

    '''
    Shows all the reviews posted, with related image and rating
    '''
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_upload_ysg4yv', blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(
        choices=RATING_CHOICES, default=0, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        Ordering reviews by the most recents ones
        '''
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product_title} reviewed by {self.owner}'
