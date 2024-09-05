from rest_framework import serializers
from .models import Diploma

class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = ['id', 'student', 'diploma_type', 'issuance_date', 'graduation_date']
