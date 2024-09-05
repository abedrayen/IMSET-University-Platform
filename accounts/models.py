from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    two_factor_code = models.CharField(max_length=6, blank=True, null=True)
    two_factor_code_expires_at = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cin_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    location_of_birth = models.CharField(max_length=100, null=True, blank=True)
