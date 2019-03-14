from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import NoReverseMatch

class ModelTestCase(TestCase):
    """This class defines the test suite for the task model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Write world class code"
        self.task = Task(name=self.name)

    def test_model_can_create_a_task(self):
        """Test the task model can create a task."""
        old_count = Task.objects.count()
        self.task.save()
        new_count = Task.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.task_data = {'name': 'Go to Shiraz'}
        
        self.response = self.client.post(
            NoReverseMatch('create'),
            self.task_data,
            format="json")

    def test_api_can_create_a_task(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_task(self):
        """Test the api can get a given task."""
        Task = task.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': Task.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, Task)

    def test_api_can_update_Task(self):
        """Test the api can update a given Task."""
        change_Task = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': Task.id}),
            change_Task, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_Task(self):
        """Test the api can delete a Task."""
        Task = task.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': Task.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)