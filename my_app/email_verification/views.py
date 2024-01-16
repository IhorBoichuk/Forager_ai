"""
Module: views.py.

Description: Contains views for handling email verification results.
"""

from typing import Any

# Django-rest imports
from rest_framework import generics, status
from rest_framework.response import Response

# Imports from my application
from email_verification.models import EmailVerificationResult
from email_verification.pyhunter import PyHunter
from email_verification.serializers import EmailVerificationResultSerializer
from my_app.settings import API_KEY


class EmailVerificationResultListCreateView(generics.ListCreateAPIView):
    """
    List and create view for EmailVerificationResult instances.

    This view allows listing all EmailVerificationResult instances and creating
    a new EmailVerificationResult by verifying an email address.

    Attributes:
        queryset (QuerySet): The set of EmailVerificationResult instances.
        serializer_class (Serializer): The serializer class for
        EmailVerificationResult.
    """

    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Create and verify email.

        Args:
            request: The HTTP request object.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            Response: The response indicating the result of the creation.
        """
        email = request.data.get('email')
        my_object = PyHunter(api_key=API_KEY)
        verification_result = my_object.email_verifier(email=email, raw=False)

        result_data = {
            'email': email,
            'verification_result': verification_result,
        }
        serializer = self.get_serializer(data=result_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmailVerificationResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detail view for EmailVerificationResult instances."""

    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer


class EmailVerificationResultListView(generics.ListAPIView):
    """List view for EmailVerificationResult instances."""

    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer


class EmailVerificationResultDeleteView(generics.DestroyAPIView):
    """
    Delete email.

    This view allows the deletion of an EmailVerificationResult instance.

    Attributes:
        queryset (QuerySet): The set of EmailVerificationResult instances.
        serializer_class (Serializer): The serializer class for
        EmailVerificationResult.
        lookup_field (str): The field to use for object lookup.
    """

    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer
    lookup_field = 'pk'

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Delete email.

        Args:
            request (Any): The request object.
            args (Any): Additional positional arguments.
            kwargs (Any): Additional keyword arguments.

        Returns:
            Response: The response indicating the result of the deletion.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
