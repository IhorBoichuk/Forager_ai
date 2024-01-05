from django.db import models


class EmailVerificationResult(models.Model):
    email = models.EmailField()
    verification_result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email