from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
import datetime

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Task."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DoTaskView(generics.UpdateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        taskId=kwargs['pk']
        partial = True
        instance = self.get_object()
        instance.completionDate = datetime.datetime.now()
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            return Response(serializer.data)

class UndoTaskView(generics.UpdateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        taskId=kwargs['pk']
        partial = True
        instance = self.get_object()
        instance.completionDate = None
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            return Response(serializer.data)