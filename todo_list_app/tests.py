from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Todo


class TodoAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        # Create a sample todo
        self.todo = Todo.objects.create(
            title="Sample Todo",
            description="This is a sample todo.",
            status="PENDING",
            user=self.user,
        )

    # ✅ Test Create Todo
    def test_create_todo(self):
        url = reverse("todo-list")  # Update the name if needed
        data = {
            "title": "New Todo",
            "description": "Test Description",
            "status": "PENDING",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Todo")

    # ✅ Test Get Todo List
    def test_get_todo_list(self):
        url = reverse("todo-list")  # Update the name if needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure at least one todo exists

    # ✅ Test Update Todo
    def test_update_todo(self):
        url = reverse(
            "todo-detail", kwargs={"pk": self.todo.id}
        )  # Update the name if needed
        data = {
            "title": "Updated Todo",
            "description": "Updated Description",
            "status": "IN_PROGRESS",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Todo")

    # ✅ Test Delete Todo
    def test_delete_todo(self):
        url = reverse(
            "todo-detail", kwargs={"pk": self.todo.id}
        )  # Update the name if needed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())
