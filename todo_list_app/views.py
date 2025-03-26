from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔹 Require authentication

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 🔹 Assign todo to the logged-in user
