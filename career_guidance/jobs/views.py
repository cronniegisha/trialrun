from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import update_jobs

class JobUpdateAPIView(APIView):
    def post(self, request):
        update_jobs.delay()
        return Response({"message": "Job update started"}, status=202)

class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
