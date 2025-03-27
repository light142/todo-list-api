from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔹 Require authentication

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)  # 🔹 Show only user's todos

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 🔹 Assign todo to the logged-in user


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(
            user=self.request.user
        )  # 🔹 Prevent users from accessing others' todos
