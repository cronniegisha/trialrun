from django.urls import path
from .views import JobListAPIView, JobUpdateAPIView


urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='job-list'),
    path('update-jobs/', JobUpdateAPIView.as_view(), name='update-jobs'),
]
