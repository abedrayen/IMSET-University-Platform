from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class Diploma(models.Model):
    DIPLOMA_TYPE_CHOICES = [
        ('BTP', 'BTP'),
        ('BTS', 'BTS'),
    ]

    student = models.ForeignKey(
        User,
        limit_choices_to={'user_type': 'student'},  
        on_delete=models.CASCADE
    )
    diploma_type = models.CharField(max_length=3, choices=DIPLOMA_TYPE_CHOICES)
    issuance_date = models.DateField()
    graduation_date = models.DateField()
    
    def __str__(self):
        return f"{self.student.first_name} - {self.get_diploma_type_display()}"
