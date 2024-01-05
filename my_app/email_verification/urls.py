from django.urls import path
from .views import (
    EmailVerificationResultListCreateView,
    EmailVerificationResultDetailView,
    EmailVerificationResultListView,
    EmailVerificationResultDeleteView,
)


urlpatterns = [
    path('results/', EmailVerificationResultListCreateView.as_view(), name='result-list'),
    path('results/<int:pk>/', EmailVerificationResultDetailView.as_view(), name='result-detail'),
    path('all-results/', EmailVerificationResultListView.as_view(), name='all-results'),
    path('results/<int:pk>/delete/', EmailVerificationResultDeleteView.as_view(), name='result-delete'),
]
