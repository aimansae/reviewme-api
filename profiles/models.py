from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    '''
    Model to store user Profile information
    '''

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=True)
    # title
    description = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-user-profile_yhtts1'
    )

    class Meta:
        '''
        Displays the most recently created profiles first
        '''
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    '''
    Creates a profile, everytime a user is created.
    (credit Code Institute Walkthrogh video)
    '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
