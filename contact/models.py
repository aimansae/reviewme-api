from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Contact(models.Model):
    '''
    Contact Form model for enquiries
    '''
    # for phone field validation:
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',  # allow + prefix, and between 9 and 15 digits
        message="Phone number must be entered in the format: '+123456789'. Up to 15 digits allowed."

    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(validators=[phone_regex], max_length=20)
    query_text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Enquiry from {self.full_name} on {self.created_at}'
