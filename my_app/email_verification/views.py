"""
Module: views.py
Description: Contains views for handling email verification results.
"""
from typing import Any

# Imports from my application
from email_verification.pyhunter import PyHunter
from email_verification.models import EmailVerificationResult
from email_verification.serializers import EmailVerificationResultSerializer
from my_app.settings import API_KEY

# Django-rest imports
from rest_framework import generics, status
from rest_framework.response import Response


class EmailVerificationResultListCreateView(generics.ListCreateAPIView) 
    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        '''
        Create and verify email
        '''
        email = request.data.get('email')
        my_object = PyHunter(api_key=API_KEY)
        verification_result = my_object.email_verifier(email=email, raw=False)
        
        result_data = {'email': email, 'verification_result': verification_result}
        serializer = self.get_serializer(data=result_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmailVerificationResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer


class EmailVerificationResultListView(generics.ListAPIView):
    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer


class EmailVerificationResultDeleteView(generics.DestroyAPIView):
    queryset = EmailVerificationResult.objects.all()
    serializer_class = EmailVerificationResultSerializer
    lookup_field = 'pk'

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        '''
        Delete email
        '''
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)