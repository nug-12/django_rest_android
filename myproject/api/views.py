from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.Retrieve.UpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create your views here.
