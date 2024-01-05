from rest_framework import serializers
from .models import EmailVerificationResult

class EmailVerificationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationResult
        fields = '__all__'
